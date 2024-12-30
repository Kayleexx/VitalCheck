from typing import Dict
import logging

class UserInterface:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def get_user_input(self) -> Dict[str, str]:
        """Get health-related information from user"""
        print("\n=== I'm VitalCheck: Your pookie health consultant ===")
        print("\nIMPORTANT: This system provides general health information only.")
        print("Always consult healthcare professionals for medical advice.")
        
        symptoms = input("\nDescribe your symptoms or health goals: ").strip()
        additional_info = input("Any additional relevant information (age range, general health status, etc.)? ").strip()
        
        return {
            "symptoms": symptoms,
            "additional_info": additional_info
        }
    
    def show_report_preview(self, report_path: str) -> None:
        try:
            print(f"\nHealth information report saved to: {report_path}")
            print("\nPreview of report:")
            print("-" * 50)
            with open(report_path, 'r', encoding='utf-8') as f:
                preview = f.read()[:500]
            print(preview + "...\n")
        except Exception as e:
            self.logger.error(f"Error showing report preview: {str(e)}")
            print("\nError: Could not display report preview")
