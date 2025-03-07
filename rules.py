import os
import time
import sys
from datetime import datetime

# ANSI color codes for terminal styling
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_logo():
    """Display a center-aligned ASCII logo."""
    # Get terminal width for centering (default to 80 if unable to determine)
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80
    
    # Logo components with their raw widths (without color codes)
    tiled_width = 41  # Width of the TILED ASCII art
    rules_width = 47  # Width of the RULES ASCII art
    generator_width = 72  # Width of the GENERATOR ASCII art
    
    # Calculate padding for each line
    tiled_padding = (terminal_width - tiled_width) // 2
    rules_padding = (terminal_width - rules_width) // 2
    generator_padding = (terminal_width - generator_width) // 2
    
    # Ensure minimum padding of at least 1 space
    tiled_padding = max(1, tiled_padding)
    rules_padding = max(1, rules_padding)
    generator_padding = max(1, generator_padding)
    
    # Create the centered logo
    logo = f"""
{" " * tiled_padding}{Colors.YELLOW}████████╗██╗██╗     ███████╗██████╗ 
{" " * tiled_padding}{Colors.YELLOW}╚══██╔══╝██║██║     ██╔════╝██╔══██╗
{" " * tiled_padding}{Colors.YELLOW}   ██║   ██║██║     █████╗  ██║  ██║
{" " * tiled_padding}{Colors.YELLOW}   ██║   ██║██║     ██╔══╝  ██║  ██║
{" " * tiled_padding}{Colors.YELLOW}   ██║   ██║███████╗███████╗██████╔╝
{" " * tiled_padding}{Colors.YELLOW}   ╚═╝   ╚═╝╚══════╝╚══════╝╚═════╝ 

{" " * rules_padding}{Colors.GREEN}██████╗ ██╗   ██╗██╗     ███████╗███████╗
{" " * rules_padding}{Colors.GREEN}██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
{" " * rules_padding}{Colors.GREEN}██████╔╝██║   ██║██║     █████╗  ███████╗
{" " * rules_padding}{Colors.GREEN}██╔══██╗██║   ██║██║     ██╔══╝  ╚════██║
{" " * rules_padding}{Colors.GREEN}██║  ██║╚██████╔╝███████╗███████╗███████║
{" " * rules_padding}{Colors.GREEN}╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝

{" " * generator_padding}{Colors.CYAN}██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
{" " * generator_padding}{Colors.CYAN}██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
{" " * generator_padding}{Colors.CYAN}██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
{" " * generator_padding}{Colors.CYAN}██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
{" " * generator_padding}{Colors.CYAN}╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
{" " * generator_padding}{Colors.CYAN} ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{Colors.END}"""
    print(logo)
    print(f"{Colors.BOLD}Generator{Colors.END} v1.0 | {Colors.CYAN}Created for Tiled Automapping{Colors.END}")
    print(f"Started: {Colors.YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.END}\n")

def typing_effect(text, delay=0.01):
    """Create a typing effect when displaying text."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def progress_bar(total, current, bar_length=40):
    """Display a progress bar."""
    percent = current / total
    arrow = "█" * int(round(percent * bar_length))
    spaces = " " * (bar_length - len(arrow))
    
    sys.stdout.write(f"\r{Colors.BLUE}Progress: [{Colors.GREEN}{arrow}{Colors.BLUE}{spaces}] {Colors.YELLOW}{int(percent * 100)}%{Colors.END}")
    sys.stdout.flush()

def print_exit_instructions():
    """Print instructions on how to exit the program."""
    print(f"\n{Colors.YELLOW}Note: You can type '{Colors.RED}exit{Colors.YELLOW}' at any input prompt to quit the program.{Colors.END}")

def check_for_exit(input_str):
    """Check if user wants to exit and handle accordingly."""
    if input_str.lower() == 'exit':
        print(f"\n{Colors.YELLOW}Exiting program as requested. Goodbye!{Colors.END}")
        sys.exit(0)
    return input_str

def get_valid_directory(prompt, base_dir=None):
    """Get a valid directory path from the user with option to retry or exit."""
    while True:
        directory = input(prompt).strip()
        check_for_exit(directory)
        
        # Check if it's a relative path that needs to be combined with base_dir
        if base_dir and not os.path.isabs(directory):
            full_path = os.path.join(base_dir, directory)
        else:
            full_path = directory
            
        if os.path.isdir(full_path):
            return full_path
        else:
            print(f"\n{Colors.RED}Error: The folder '{directory}' doesn't exist.{Colors.END}")
            choice = input(f"{Colors.YELLOW}Would you like to try again? (Y/n): {Colors.END}").strip().lower()
            check_for_exit(choice)
            if choice == 'n':
                return None

def collect_directories():
    """Get the main folder and rule folders from the user."""
    typing_effect(f"{Colors.CYAN}Welcome to the Tiled rules.txt generator!{Colors.END}")
    typing_effect(f"{Colors.CYAN}This tool creates a rules.txt file for Tiled's Automapping feature.{Colors.END}\n")
    
    print_exit_instructions()
    
    # Get main project directory
    root_dir = get_valid_directory(f"{Colors.BOLD}{Colors.YELLOW}Step 1/3{Colors.END} - Where is your main Tiled project folder located?\n{Colors.GREEN}>{Colors.END} ")
    
    if not root_dir:
        print(f"\n{Colors.RED}No valid main folder provided. Program cannot continue.{Colors.END}")
        return None, []
        
    # Get number of rule directories
    while True:
        try:
            num_dirs_input = input(f"\n{Colors.BOLD}{Colors.YELLOW}Step 2/3{Colors.END} - How many folders containing rule files (.tmx) do you want to include?\n{Colors.GREEN}>{Colors.END} ")
            check_for_exit(num_dirs_input)
            num_dirs = int(num_dirs_input)
            if num_dirs <= 0:
                print(f"{Colors.YELLOW}Please enter a positive number.{Colors.END}")
                continue
            break
        except ValueError:
            print(f"\n{Colors.RED}Error: Please enter a valid number.{Colors.END}")

    directories = []
    i = 0
    while i < num_dirs:
        subdir = input(f"{Colors.CYAN}Enter folder {i + 1} (location inside '{root_dir}'):{Colors.END}\n{Colors.GREEN}>{Colors.END} ").strip()
        check_for_exit(subdir)
        
        full_path = os.path.join(root_dir, subdir)
        if os.path.isdir(full_path):
            directories.append(full_path)
            print(f"{Colors.GREEN}✓ Folder added{Colors.END}")
            i += 1
        else:
            print(f"{Colors.YELLOW}⚠️  Warning: The folder '{subdir}' doesn't exist.{Colors.END}")
            choice = input(f"{Colors.YELLOW}Would you like to try again? (Y/n): {Colors.END}").strip().lower()
            check_for_exit(choice)
            if choice == 'n':
                i += 1  # Skip this folder entry

    # Allow reviewing and changing folders
    if directories:
        print(f"\n{Colors.CYAN}Folders selected for scanning:{Colors.END}")
        for idx, directory in enumerate(directories):
            print(f"{Colors.YELLOW}{idx + 1}.{Colors.END} {os.path.relpath(directory, root_dir)}")
            
        while True:
            change = input(f"\n{Colors.YELLOW}Would you like to change any of these folders? (y/N): {Colors.END}").strip().lower()
            check_for_exit(change)
            
            if change == 'y':
                try:
                    folder_num = int(input(f"{Colors.YELLOW}Enter the number of the folder to change (1-{len(directories)}): {Colors.END}"))
                    if 1 <= folder_num <= len(directories):
                        current_folder = os.path.relpath(directories[folder_num - 1], root_dir)
                        new_subdir = input(f"{Colors.CYAN}Enter new folder to replace '{current_folder}':{Colors.END}\n{Colors.GREEN}>{Colors.END} ").strip()
                        check_for_exit(new_subdir)
                        
                        new_full_path = os.path.join(root_dir, new_subdir)
                        if os.path.isdir(new_full_path):
                            directories[folder_num - 1] = new_full_path
                            print(f"{Colors.GREEN}✓ Folder updated{Colors.END}")
                        else:
                            print(f"{Colors.RED}Error: The folder '{new_subdir}' doesn't exist.{Colors.END}")
                            retry = input(f"{Colors.YELLOW}Would you like to try another path? (Y/n): {Colors.END}").strip().lower()
                            check_for_exit(retry)
                            if retry != 'n':
                                continue
                    else:
                        print(f"{Colors.RED}Invalid folder number.{Colors.END}")
                except ValueError:
                    print(f"{Colors.RED}Please enter a valid number.{Colors.END}")
                
                # Show updated list
                print(f"\n{Colors.CYAN}Updated folders for scanning:{Colors.END}")
                for idx, directory in enumerate(directories):
                    print(f"{Colors.YELLOW}{idx + 1}.{Colors.END} {os.path.relpath(directory, root_dir)}")
                
                continue_changing = input(f"{Colors.YELLOW}Change another folder? (y/N): {Colors.END}").strip().lower()
                check_for_exit(continue_changing)
                if continue_changing != 'y':
                    break
            else:
                break

    return root_dir, directories


def find_tmx_files(root_dir, directories):
    """Find all .tmx files in the specified folders."""
    print(f"\n{Colors.BLUE}Scanning directories for .tmx files...{Colors.END}")
    
    tmx_files = []
    total_dirs = len(directories)
    
    for i, directory in enumerate(directories):
        # Display directory being scanned
        print(f"{Colors.CYAN}Scanning: {directory}{Colors.END}")
        
        for root, _, files in os.walk(directory):
            tmx_in_dir = [f for f in files if f.endswith(".tmx")]
            if tmx_in_dir:
                print(f"  {Colors.GREEN}Found {len(tmx_in_dir)} .tmx files in {os.path.relpath(root, directory)}{Colors.END}")
                
                for file in tmx_in_dir:
                    full_path = os.path.join(root, file)
                    relative_path = os.path.relpath(full_path, start=root_dir)
                    tmx_files.append(relative_path.replace("\\", "/"))
        
        # Show progress
        progress_bar(total_dirs, i + 1)
        
    print(f"\n{Colors.GREEN}Scan complete! Found {len(tmx_files)} total .tmx files{Colors.END}")
    return tmx_files


def write_rules_txt(tmx_files):
    """Create the rules.txt file with all the .tmx files."""
    print(f"\n{Colors.CYAN}Creating rules.txt file...{Colors.END}")
    time.sleep(0.5)  # Slight delay for effect
    
    # Show writing progress
    total = len(tmx_files)
    for i in range(total):
        progress_bar(total, i + 1)
        time.sleep(0.01)  # Quick but visible progress
    
    with open("rules.txt", "w", encoding="utf-8") as rules_file:
        for tmx_file in tmx_files:
            rules_file.write(f"{tmx_file}\n")
    
    print(f"\n\n{Colors.GREEN}✅ Done! 'rules.txt' has been created with {len(tmx_files)} rule files.{Colors.END}")
    print(f"{Colors.YELLOW}Place this 'rules.txt' file in your main Tiled project folder to enable Automapping.{Colors.END}\n")


def main():
    # Clear screen for a fresh start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print_logo()
    
    root_dir, directories = collect_directories()

    if not root_dir or not directories:
        print(f"\n{Colors.RED}❌ No valid folders provided. Program ended.{Colors.END}")
        return

    print(f"\n{Colors.BOLD}{Colors.YELLOW}Step 3/3{Colors.END} - Searching for rule files...")
    tmx_files = find_tmx_files(root_dir, directories)

    if not tmx_files:
        print(f"\n{Colors.RED}❌ No .tmx files found in the folders you specified.{Colors.END}")
    else:
        # Confirm before creating rules.txt
        confirm = input(f"\n{Colors.YELLOW}Ready to create rules.txt with {len(tmx_files)} files. Continue? (Y/n): {Colors.END}").strip().lower()
        check_for_exit(confirm)
        
        if confirm != 'n':
            write_rules_txt(tmx_files)
            
            # Final success message
            print(f"{Colors.BOLD}{Colors.GREEN}You can now use these rules in Tiled's Automapping feature.{Colors.END}")
            print(f"\n{Colors.CYAN}Thanks for using Tiled Rules.txt Generator!{Colors.END}")
        else:
            print(f"\n{Colors.YELLOW}Operation cancelled. No rules.txt file was created.{Colors.END}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Process interrupted by user. Exiting...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {str(e)}{Colors.END}")
    finally:
        print(f"\n{Colors.CYAN}© {datetime.now().year} Tiled Rules Generator{Colors.END}")