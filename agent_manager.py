# agent_manager.py
from scrapybara import Scrapybara
import logging
import time  # Added missing import
from typing import Dict, Any
from dataclasses import dataclass

@dataclass
class AgentState:
    status: str
    last_update: float
    retry_count: int = 0
    max_retries: int = 1

class AgentManager:
    def __init__(self, api_key: str):
        self.logger = logging.getLogger(__name__)
        self.client = Scrapybara(api_key=api_key)
        self.agents = {}
        self.agent_states = {}
    
    def start_agent(self, agent_id: str, instance_type: str = "small") -> None:
        try:
            if agent_id in self.agents:
                self.logger.info(f"Agent {agent_id} already running")
                return
                
            self.agents[agent_id] = self.client.start(instance_type=instance_type)
            self.agent_states[agent_id] = AgentState(
                status="running", 
                last_update=time.time()
            )
            self.logger.info(f"Started agent: {agent_id}")
        except Exception as e:
            self.logger.error(f"Failed to start agent {agent_id}: {str(e)}")
            # Clean up if agent was partially created
            if agent_id in self.agents:
                del self.agents[agent_id]
            if agent_id in self.agent_states:
                del self.agent_states[agent_id]
            raise
    
    def process_health_query(self, user_input: Dict[str, str]) -> str:
        try:
            self.start_agent("research")
            research_output = self._execute_with_retry(
                "research",
                lambda: self._perform_research(user_input)
            )
            return research_output
        except Exception as e:
            self.logger.error(f"Error processing health query: {str(e)}")
            raise
    
    def _perform_research(self, user_input: Dict[str, str]) -> str:
        try:
            agent = self.agents.get("research")
            if not agent:
                raise ValueError("Research agent not initialized")
                
            query = self._format_research_query(user_input)
            task = agent.agent.act(cmd=query, include_screenshot=False)
            
            if not hasattr(task, 'output'):
                raise ValueError("No output received from research task")
                
            return task.output if isinstance(task.output, str) else str(task.output)
            
        except Exception as e:
            self.logger.error(f"Error performing research: {str(e)}")
            raise
    
    def _execute_with_retry(self, agent_id: str, operation: callable) -> Any:
        state = self.agent_states.get(agent_id)
        if not state:
            raise ValueError(f"No state found for agent {agent_id}")
            
        while state.retry_count < state.max_retries:
            try:
                return operation()
            except Exception as e:
                state.retry_count += 1
                self.logger.warning(f"Attempt {state.retry_count} failed for {agent_id}: {str(e)}")
                if state.retry_count >= state.max_retries:
                    raise
                wait_time = 2 ** state.retry_count
                self.logger.info(f"Waiting {wait_time} seconds before retry...")
                time.sleep(wait_time)  # Exponential backoff
    
    def cleanup(self) -> None:
        for agent_id, agent in list(self.agents.items()):
            try:
                agent.stop()
                self.logger.info(f"Stopped agent: {agent_id}")
            except Exception as e:
                self.logger.error(f"Error stopping agent {agent_id}: {str(e)}")
            finally:
                # Clean up internal state regardless of stop success
                self.agents.pop(agent_id, None)
                self.agent_states.pop(agent_id, None)

    @staticmethod
    def _format_research_query(user_input: Dict[str, str]) -> str:
        return f"""Research health information about the following:
    
Symptoms/Goals: {user_input['symptoms']}
Additional Information: {user_input['additional_info']}

Please provide:
1. General information about these symptoms/goals
2. Common causes or factors
3. General wellness recommendations
4. When to seek professional medical care

Note: Format the information clearly and include reliable general health guidelines."""