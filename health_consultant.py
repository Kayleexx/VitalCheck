from agent_manager import AgentManager
from user_interface import UserInterface
from report_generator import ReportGenerator
from config import load_config
import logging
from typing import Optional

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('health_consultant.log'),
            logging.StreamHandler()
        ]
    )

def main():
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Initialize components that don't require config
    ui = UserInterface()
    agent_manager: Optional[AgentManager] = None
    
    try:
        # Load configuration
        config = load_config()
        
        # Initialize components that require config
        agent_manager = AgentManager(config['api_key'])
        report_generator = ReportGenerator()
        
        # Get user input
        user_input = ui.get_user_input()
        
        # Process health information
        research_output = agent_manager.process_health_query(user_input)
        
        # Generate and save report
        report_path = report_generator.generate_and_save(research_output, user_input)
        
        # Show results to user
        ui.show_report_preview(report_path)
        
    except ValueError as ve:
        # Handle configuration errors specifically
        logger.error(f"Configuration error: {str(ve)}")
        print(f"\nConfiguration Error: {str(ve)}")
        print("Please ensure your .env file is set up correctly with your API key.")
        
    except Exception as e:
        # Handle other unexpected errors
        logger.error(f"Error in main process: {str(e)}", exc_info=True)
        print(f"\nAn error occurred: {str(e)}")
    
    finally:
        # Only cleanup if agent_manager was initialized
        if agent_manager is not None:
            try:
                agent_manager.cleanup()
            except Exception as e:
                logger.error(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    main()
