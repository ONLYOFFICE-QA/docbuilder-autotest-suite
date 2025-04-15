import os
from lib.static_data import TMP_FOLDER

class ScriptJS:
    def __init__(self):
        self.temp_files = []
    
    def prepare_script(self, script_path: str) -> (str, str):
        """
        Checks if the JS script contains 'docbuilder' in the first 10 rows and last 10 rows.
        If not found in first 10 rows, adds 'builder.CreateFile("docx");' to the beginning.
        If not found in last 10 rows, adds save and close commands to the end.
        
        Args:
            script_path (str): Path to the JavaScript script file.
            
        Returns:
            str: Path to the prepared script file (could be the original or a modified one).
        """
        # Make sure the script path exists
        if not os.path.isfile(script_path):
            raise FileNotFoundError(f"Script file not found at: {script_path}")
            
        # Get the script name without extension for the output filename
        script_name = os.path.splitext(os.path.basename(script_path))[0]
        output_filename = os.path.join(TMP_FOLDER, f"{script_name}.docx")
            
        with open(script_path, 'r') as file:
            lines = file.readlines()
            
        # Check if 'docbuilder' is in the first 10 rows
        has_docbuilder_start = False
        for i in range(min(10, len(lines))):
            if 'docbuilder' in lines[i].lower():
                has_docbuilder_start = True
                break
        
        # Check if 'docbuilder' is in the last 10 rows
        has_docbuilder_end = False
        for i in range(max(0, len(lines) - 10), len(lines)):
            if 'docbuilder' in lines[i].lower():
                has_docbuilder_end = True
                break
        
        # Create a new file if modifications are needed
        if not has_docbuilder_start or not has_docbuilder_end:
            new_lines = lines.copy()
            
            # If 'docbuilder' is not found at the start, add the line to create a docx file
            if not has_docbuilder_start:
                new_lines = ['builder.CreateFile("docx");\n'] + new_lines
            
            # If 'docbuilder' is not found at the end, add the save and close commands
            if not has_docbuilder_end:
                # Make sure there's a newline before adding the new commands
                if new_lines and not new_lines[-1].endswith('\n'):
                    new_lines[-1] += '\n'
                
                new_lines.append(f'builder.SaveFile("docx", "{output_filename}");\n')
                new_lines.append('builder.CloseFile();\n')
            
            # Create a temporary file with the modified content
            temp_script_path = os.path.join(TMP_FOLDER, f"{script_name}_temp.js")
            with open(temp_script_path, 'w') as file:
                file.writelines(new_lines)
            
            # Keep track of temp files for cleanup
            self.temp_files.append(temp_script_path)
            
            return temp_script_path, output_filename
        
        # Return the original path if no modification was needed
        return script_path, output_filename
        
    def cleanup(self) -> None:
        """
        Clean up any temporary files created during script preparation.
        """
        for temp_file in self.temp_files:
            if os.path.exists(temp_file):
                try:
                    os.remove(temp_file)
                except Exception as e:
                    print(f"Warning: Failed to remove temporary file {temp_file}: {e}")
        
        self.temp_files = []
