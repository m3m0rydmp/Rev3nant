#!/usr/bin/env python3
"""
Security Awareness Tool - Python Version
Converted from React component to tkinter application
"""

import tkinter as tk
from tkinter import ttk, messagebox
import time
import math
import threading
from datetime import datetime
import platform
import os
import socket
import getpass
import json
import base64
import subprocess
from cryptography.fernet import Fernet

class SecurityAwarenessTool:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Security Awareness Assessment")
        self.root.configure(bg='black')
        
        # Make fullscreen
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        
        # Bind escape key to exit fullscreen
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        
        # State variables
        self.current_step = 0
        self.start_time = datetime.now()
        self.show_warning = True
        self.animation_running = True
        
        # Steps configuration
        self.steps = [
            {
                "title": "⚠️ SECURITY ASSESSMENT FAILED",
                "type": "error",
                "content": "You have just executed an unknown program from an untrusted USB device!"
            },
            {
                "title": "🔴 POTENTIAL CONSEQUENCES",
                "type": "warning",
                "content": "In a real attack, this could have resulted in:"
            },
            {
                "title": "🛡️ WHAT YOU SHOULD DO",
                "type": "info",
                "content": "Best practices to protect yourself and your organization:"
            }
        ]
        
        # Content data
        self.consequences = [
            "💀 Ransomware encrypting all company files",
            "🔑 Keyloggers capturing passwords and sensitive data",
            "🎯 Remote access trojans giving attackers full control",
            "💸 Financial data stolen and sold on dark web",
            "📊 Customer information compromised",
            "🌐 Network-wide infrastructure infiltration"
        ]
        
        self.best_practices = [
            "✅ NEVER plug in unknown USB devices",
            "✅ Always scan external media with updated antivirus",
            "✅ Verify suspicious files with IT Security team",
            "✅ Report found USB devices to security personnel",
            "✅ Keep your system and software updated",
            "✅ Enable real-time protection and firewalls"
        ]
        
        # Initialize UI
        self.setup_ui()
        
        # Start animations
        self.start_animations()
        
        # Auto-advance timer
        self.auto_advance_timer()
        
        # Collect system info silently
        self.collect_system_info()
    

    
    def setup_ui(self):
        """Setup the main UI components"""
        # Get screen dimensions for responsive design
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate responsive padding and font sizes
        self.padding = min(20, max(5, min(screen_width, screen_height) // 100))
        # Increase minimum font scale for better readability on small screens
        self.font_scale = min(1.2, max(0.8, min(screen_width, screen_height) / 1000))
        
        # Main container with responsive padding
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.pack(fill='both', expand=True, padx=self.padding, pady=self.padding)
        
        # Animated background (simplified grid effect)
        self.bg_canvas = tk.Canvas(self.main_frame, bg='black', highlightthickness=0)
        self.bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Main content container with responsive padding
        self.content_frame = tk.Frame(self.main_frame, bg='#1a1a1a', relief='solid', bd=2)
        self.content_frame.pack(fill='both', expand=True, padx=self.padding//2, pady=self.padding//2)
        
        # Header
        self.setup_header()
        
        # Progress bar
        self.setup_progress_bar()
        
        # Content area
        self.setup_content_area()
        
        # Footer
        self.setup_footer()
    
    def setup_header(self):
        """Setup the header section"""
        header_frame = tk.Frame(self.content_frame, bg='#7f1d1d', relief='solid', bd=2)
        header_frame.pack(fill='x', padx=self.padding//2, pady=(self.padding//2, 5))
        
        # Title with warning icons
        title_frame = tk.Frame(header_frame, bg='#7f1d1d')
        title_frame.pack(pady=self.padding)
        
        # Calculate responsive font sizes
        title_font_size = max(18, int(24 * self.font_scale))
        subtitle_font_size = max(10, int(12 * self.font_scale))
        
        # Warning icons
        self.warning_icon1 = tk.Label(title_frame, text="⚠️", font=('Arial', title_font_size), 
                                     bg='#7f1d1d', fg='#fca5a5')
        self.warning_icon1.pack(side='left', padx=self.padding//2)
        
        # Main title
        self.title_label = tk.Label(title_frame, text=self.steps[0]["title"], 
                                   font=('Arial', title_font_size, 'bold'), bg='#7f1d1d', fg='#fca5a5')
        self.title_label.pack(side='left', padx=self.padding)
        
        self.warning_icon2 = tk.Label(title_frame, text="⚠️", font=('Arial', title_font_size), 
                                     bg='#7f1d1d', fg='#fca5a5')
        self.warning_icon2.pack(side='left', padx=self.padding//2)
        
        # Subtitle
        subtitle_label = tk.Label(header_frame, text="USB Drop Attack Simulation - Educational Purpose",
                                 font=('Arial', subtitle_font_size), bg='#7f1d1d', fg='#67e8f9')
        subtitle_label.pack(pady=(0, self.padding))
    
    def setup_progress_bar(self):
        """Setup the progress bar"""
        progress_frame = tk.Frame(self.content_frame, bg='#374151')
        progress_frame.pack(fill='x', padx=self.padding//2, pady=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, 
                                           maximum=100, mode='determinate')
        self.progress_bar.pack(fill='x', pady=self.padding//2, padx=self.padding)
        
        # Step indicator and navigation
        nav_frame = tk.Frame(progress_frame, bg='#374151')
        nav_frame.pack(fill='x', pady=(0, self.padding//2), padx=self.padding)
        
        # Calculate responsive font sizes
        step_font_size = max(10, int(12 * self.font_scale))
        button_font_size = max(9, int(10 * self.font_scale))
        
        # Step indicator
        self.step_label = tk.Label(nav_frame, text="Step 1 of 3", 
                                  font=('Arial', step_font_size, 'bold'), bg='#374151', fg='#9ca3af')
        self.step_label.pack(side='left')
        
        # Navigation buttons
        button_frame = tk.Frame(nav_frame, bg='#374151')
        button_frame.pack(side='right')
        
        # Previous button
        self.prev_button = tk.Button(button_frame, text="◀ Previous", 
                                    font=('Arial', button_font_size, 'bold'), bg='#374151', fg='#9ca3af',
                                    command=self.previous_step, relief='flat', 
                                    padx=int(15 * self.font_scale), pady=int(5 * self.font_scale))
        self.prev_button.pack(side='left', padx=5)
        
        # Next button
        self.next_button = tk.Button(button_frame, text="Next ▶", 
                                    font=('Arial', button_font_size, 'bold'), bg='#374151', fg='#9ca3af',
                                    command=self.next_step, relief='flat', 
                                    padx=int(15 * self.font_scale), pady=int(5 * self.font_scale))
        self.next_button.pack(side='left', padx=5)
        
        # Update button states
        self.update_navigation_buttons()
    
    def setup_content_area(self):
        """Setup the main content area"""
        self.content_area = tk.Frame(self.content_frame, bg='#1a1a1a')
        self.content_area.pack(fill='both', expand=True, padx=self.padding, pady=self.padding)
        
        # Initialize first step
        self.show_step_content()
    
    def setup_footer(self):
        """Setup the footer"""
        footer_frame = tk.Frame(self.content_frame, bg='#374151', relief='solid', bd=1)
        footer_frame.pack(fill='x', padx=self.padding//2, pady=(5, self.padding//2))
        
        # Calculate responsive font sizes
        footer_title_size = max(10, int(12 * self.font_scale))
        footer_subtitle_size = max(8, int(9 * self.font_scale))
        
        footer_title = tk.Label(footer_frame, text="Security Awareness Training - Cybersecurity Team",
                               font=('Arial', footer_title_size, 'bold'), bg='#374151', fg='#67e8f9')
        footer_title.pack(pady=self.padding//2)
        
        footer_subtitle = tk.Label(footer_frame, text="This simulation helps protect our organization from real threats",
                                  font=('Arial', footer_subtitle_size), bg='#374151', fg='#9ca3af')
        footer_subtitle.pack(pady=(0, self.padding//2))
    
    def show_step_content(self):
        """Show content for current step"""
        # Clear previous content
        for widget in self.content_area.winfo_children():
            widget.destroy()
        
        if self.current_step == 0:
            self.show_step_0()
        elif self.current_step == 1:
            self.show_step_1()
        elif self.current_step == 2:
            self.show_step_2()
    
    def show_step_0(self):
        """Show step 0 content - Initial warning"""
        # Calculate responsive font sizes and wrap lengths
        warning_font_size = max(32, int(48 * self.font_scale))
        message_font_size = max(14, int(16 * self.font_scale))
        violation_font_size = max(10, int(12 * self.font_scale))
        explanation_font_size = max(10, int(12 * self.font_scale))
        
        # Calculate responsive wrap lengths based on screen width
        screen_width = self.root.winfo_screenwidth()
        wrap_length = min(800, max(400, int(screen_width * 0.6)))
        violation_wrap = min(700, max(350, int(screen_width * 0.5)))
        
        # Main warning icon
        warning_icon = tk.Label(self.content_area, text="⚠️", font=('Arial', warning_font_size), 
                               bg='#1a1a1a', fg='#fca5a5')
        warning_icon.pack(pady=self.padding)
        
        # Main message
        message_label = tk.Label(self.content_area, 
                                text="You have just executed an unknown program from an untrusted USB device!",
                                font=('Arial', message_font_size), bg='#1a1a1a', fg='#fca5a5',
                                wraplength=wrap_length, justify='center')
        message_label.pack(pady=self.padding)
        
        # Critical violation box
        violation_frame = tk.Frame(self.content_area, bg='#7f1d1d', relief='solid', bd=2)
        violation_frame.pack(pady=self.padding, padx=self.padding, fill='x')
        
        violation_text = tk.Label(violation_frame, 
                                 text="CRITICAL SECURITY VIOLATION DETECTED\nUnauthorized execution of external media content",
                                 font=('Arial', violation_font_size, 'bold'), bg='#7f1d1d', fg='#fecaca',
                                 wraplength=violation_wrap, justify='center')
        violation_text.pack(pady=self.padding)
        
        # Explanation
        explanation_label = tk.Label(self.content_area, 
                                    text="This is a simulated attack for educational purposes.\nIn a real scenario, your system could now be compromised.",
                                    font=('Arial', explanation_font_size), bg='#1a1a1a', fg='#d1d5db',
                                    wraplength=wrap_length, justify='center')
        explanation_label.pack(pady=self.padding)
    
    def show_step_1(self):
        """Show step 1 content - Consequences"""
        # Calculate responsive font sizes and wrap lengths
        title_font_size = max(16, int(20 * self.font_scale))
        content_font_size = max(10, int(11 * self.font_scale))
        stats_font_size = max(9, int(10 * self.font_scale))
        
        # Calculate responsive wrap lengths based on screen width
        screen_width = self.root.winfo_screenwidth()
        column_wrap = min(400, max(200, int(screen_width * 0.25)))
        
        # Title
        title_label = tk.Label(self.content_area, text="Potential Damage", 
                              font=('Arial', title_font_size, 'bold'), bg='#1a1a1a', fg='#fca5a5')
        title_label.pack(pady=self.padding)
        
        # Create two columns
        columns_frame = tk.Frame(self.content_area, bg='#1a1a1a')
        columns_frame.pack(fill='both', expand=True, padx=self.padding)
        
        # Left column - Consequences
        left_frame = tk.Frame(columns_frame, bg='#1a1a1a')
        left_frame.pack(side='left', fill='both', expand=True, padx=self.padding//2)
        
        for i, consequence in enumerate(self.consequences):
            consequence_frame = tk.Frame(left_frame, bg='#7f1d1d', relief='solid', bd=1)
            consequence_frame.pack(fill='x', pady=5)
            
            consequence_label = tk.Label(consequence_frame, text=consequence,
                                       font=('Arial', content_font_size), bg='#7f1d1d', fg='#fecaca',
                                       wraplength=column_wrap, justify='left', anchor='w')
            consequence_label.pack(pady=self.padding//2, padx=self.padding//2)
        
        # Right column - Statistics
        right_frame = tk.Frame(columns_frame, bg='#1a1a1a')
        right_frame.pack(side='right', fill='both', expand=True, padx=self.padding//2)
        
        # Ransomware costs
        costs_frame = tk.Frame(right_frame, bg='#92400e', relief='solid', bd=1)
        costs_frame.pack(fill='x', pady=5)
        
        costs_text = tk.Label(costs_frame, 
                             text="Average ransomware attack costs:\n• Small business: $84,000\n• Enterprise: $4.6M\n• Recovery time: 23 days average",
                             font=('Arial', stats_font_size), bg='#92400e', fg='#fed7aa',
                             wraplength=column_wrap, justify='left', anchor='w')
        costs_text.pack(pady=self.padding, padx=self.padding//2)
        
        # Data breach stats
        stats_frame = tk.Frame(right_frame, bg='#a16207', relief='solid', bd=1)
        stats_frame.pack(fill='x', pady=5)
        
        stats_text = tk.Label(stats_frame, 
                             text="Data breach statistics:\n• 45% caused by USB drops\n• 98% success rate in corporate environments\n• Average detection time: 287 days",
                             font=('Arial', stats_font_size), bg='#a16207', fg='#fef3c7',
                             wraplength=column_wrap, justify='left', anchor='w')
        stats_text.pack(pady=self.padding, padx=self.padding//2)
    
    def show_step_2(self):
        """Show step 2 content - Best practices"""
        # Calculate responsive font sizes and wrap lengths
        title_font_size = max(16, int(20 * self.font_scale))
        practices_title_size = max(12, int(14 * self.font_scale))
        content_font_size = max(10, int(11 * self.font_scale))
        step_font_size = max(9, int(10 * self.font_scale))
        button_font_size = max(12, int(14 * self.font_scale))
        
        # Calculate responsive wrap lengths based on screen width
        screen_width = self.root.winfo_screenwidth()
        column_wrap = min(400, max(200, int(screen_width * 0.25)))
        
        # Title
        title_label = tk.Label(self.content_area, text="Protect Yourself & Your Organization", 
                              font=('Arial', title_font_size, 'bold'), bg='#1a1a1a', fg='#86efac')
        title_label.pack(pady=self.padding)
        
        # Create two columns
        columns_frame = tk.Frame(self.content_area, bg='#1a1a1a')
        columns_frame.pack(fill='both', expand=True, padx=self.padding)
        
        # Left column - Best practices
        left_frame = tk.Frame(columns_frame, bg='#1a1a1a')
        left_frame.pack(side='left', fill='both', expand=True, padx=self.padding//2)
        
        practices_label = tk.Label(left_frame, text="Security Best Practices:", 
                                  font=('Arial', practices_title_size, 'bold'), bg='#1a1a1a', fg='#67e8f9')
        practices_label.pack(pady=self.padding//2)
        
        for practice in self.best_practices:
            practice_frame = tk.Frame(left_frame, bg='#14532d', relief='solid', bd=1)
            practice_frame.pack(fill='x', pady=3)
            
            practice_label = tk.Label(practice_frame, text=practice,
                                     font=('Arial', content_font_size), bg='#14532d', fg='#bbf7d0',
                                     wraplength=column_wrap, justify='left', anchor='w')
            practice_label.pack(pady=self.padding//2, padx=self.padding//2)
        
        # Right column - Emergency procedures
        right_frame = tk.Frame(columns_frame, bg='#1a1a1a')
        right_frame.pack(side='right', fill='both', expand=True, padx=self.padding//2)
        
        # If you find a USB device
        usb_frame = tk.Frame(right_frame, bg='#1e3a8a', relief='solid', bd=1)
        usb_frame.pack(fill='x', pady=5)
        
        usb_title = tk.Label(usb_frame, text="If You Find a USB Device:", 
                            font=('Arial', practices_title_size, 'bold'), bg='#1e3a8a', fg='#93c5fd')
        usb_title.pack(pady=self.padding//2)
        
        usb_steps = [
            "1. DON'T plug it into any computer",
            "2. Report it to IT Security immediately",
            "3. Provide details about where you found it",
            "4. Let security team handle it safely"
        ]
        
        for step in usb_steps:
            step_label = tk.Label(usb_frame, text=step,
                                 font=('Arial', step_font_size), bg='#1e3a8a', fg='#bfdbfe',
                                 wraplength=column_wrap, justify='left', anchor='w')
            step_label.pack(pady=2, padx=self.padding//2)
        
        # Emergency contacts
        contacts_frame = tk.Frame(right_frame, bg='#581c87', relief='solid', bd=1)
        contacts_frame.pack(fill='x', pady=5)
        
        contacts_title = tk.Label(contacts_frame, text="Emergency Contacts:", 
                                 font=('Arial', practices_title_size, 'bold'), bg='#581c87', fg='#c084fc')
        contacts_title.pack(pady=self.padding//2)
        
        contacts_text = tk.Label(contacts_frame, 
                                text="🔒 Alignex Cybersecurity Team\n📧 security.help@alignex.pro\n🚨 For urgent matters, send an email",
                                font=('Arial', step_font_size), bg='#581c87', fg='#ddd6fe',
                                wraplength=column_wrap, justify='left', anchor='w')
        contacts_text.pack(pady=self.padding//2, padx=self.padding//2)
        
        # Complete button
        complete_button = tk.Button(self.content_area, 
                                   text="I UNDERSTAND - COMPLETE ASSESSMENT",
                                   font=('Arial', button_font_size, 'bold'), bg='#16a34a', fg='white',
                                   command=self.handle_acknowledge,
                                   relief='flat', 
                                   padx=int(30 * self.font_scale), pady=int(15 * self.font_scale))
        complete_button.pack(pady=self.padding)
        
        # Add keyboard shortcuts
        self.root.bind('<Left>', lambda e: self.previous_step())
        self.root.bind('<Right>', lambda e: self.next_step())
        self.root.bind('<space>', lambda e: self.next_step())
    
    def handle_acknowledge(self):
        """Handle the acknowledge button click"""
        duration = round((datetime.now() - self.start_time).total_seconds())
        
        message = f"""Assessment completed in {duration} seconds.

This incident has been logged for training purposes.

Remember: Always verify unknown USB devices with IT Security!"""
        
        messagebox.showinfo("Assessment Complete", message)
        self.show_completion_screen()
    
    def show_completion_screen(self):
        """Show the completion screen"""
        self.show_warning = False
        
        # Clear main content
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Calculate responsive font sizes and padding
        check_font_size = max(32, int(48 * self.font_scale))
        title_font_size = max(18, int(24 * self.font_scale))
        msg_font_size = max(12, int(14 * self.font_scale))
        exit_font_size = max(10, int(12 * self.font_scale))
        
        # Calculate responsive padding based on screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        frame_padx = min(100, max(20, int(screen_width * 0.1)))
        frame_pady = min(100, max(20, int(screen_height * 0.1)))
        
        # Completion message
        completion_frame = tk.Frame(self.main_frame, bg='#14532d', relief='solid', bd=2)
        completion_frame.pack(expand=True, padx=frame_padx, pady=frame_pady)
        
        # Check mark icon
        check_icon = tk.Label(completion_frame, text="✓", font=('Arial', check_font_size), 
                             bg='#14532d', fg='#86efac')
        check_icon.pack(pady=self.padding)
        
        # Completion title
        completion_title = tk.Label(completion_frame, text="Assessment Complete", 
                                   font=('Arial', title_font_size, 'bold'), bg='#14532d', fg='#86efac')
        completion_title.pack(pady=self.padding)
        
        # Completion message
        completion_msg = tk.Label(completion_frame, 
                                 text="Thank you for participating in this security awareness exercise.",
                                 font=('Arial', msg_font_size), bg='#14532d', fg='#bbf7d0',
                                 wraplength=min(400, max(200, int(screen_width * 0.3))), justify='center')
        completion_msg.pack(pady=self.padding)
        
        # Exit instructions
        exit_label = tk.Label(completion_frame, 
                             text="Press ESC to exit",
                             font=('Arial', exit_font_size), bg='#14532d', fg='#bbf7d0')
        exit_label.pack(pady=self.padding)
    
    def auto_advance_timer(self):
        """Auto-advance through steps every 5 seconds"""
        if self.show_warning and self.current_step < len(self.steps) - 1:
            self.root.after(5000, self.advance_step)
    
    def advance_step(self):
        """Advance to next step"""
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_ui()
            self.auto_advance_timer()
    
    def next_step(self):
        """Manual next step"""
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
            self.update_ui()
            self.auto_advance_timer()
    
    def previous_step(self):
        """Manual previous step"""
        if self.current_step > 0:
            self.current_step -= 1
            self.update_ui()
            self.auto_advance_timer()
    
    def update_navigation_buttons(self):
        """Update navigation button states"""
        # Previous button
        if self.current_step == 0:
            self.prev_button.config(state='disabled', bg='#1f2937', fg='#6b7280')
        else:
            self.prev_button.config(state='normal', bg='#374151', fg='#9ca3af')
        
        # Next button
        if self.current_step == len(self.steps) - 1:
            self.next_button.config(state='disabled', bg='#1f2937', fg='#6b7280')
        else:
            self.next_button.config(state='normal', bg='#374151', fg='#9ca3af')
    
    def update_ui(self):
        """Update UI for current step"""
        # Update title
        self.title_label.config(text=self.steps[self.current_step]["title"])
        
        # Update progress
        progress = ((self.current_step + 1) / len(self.steps)) * 100
        self.progress_var.set(progress)
        
        # Update step indicator
        self.step_label.config(text=f"Step {self.current_step + 1} of {len(self.steps)}")
        
        # Update navigation buttons
        self.update_navigation_buttons()
        
        # Update content
        self.show_step_content()
    
    def start_animations(self):
        """Start background animations"""
        def animate_warning_icons():
            if self.animation_running:
                # Pulse animation for warning icons
                for icon in [self.warning_icon1, self.warning_icon2]:
                    current_fg = icon.cget('fg')
                    if current_fg == '#fca5a5':
                        icon.config(fg='#ef4444')
                    else:
                        icon.config(fg='#fca5a5')
                
                self.root.after(1000, animate_warning_icons)
        
        animate_warning_icons()
    
    def collect_system_info(self):
        """Collect system information silently"""
        try:
            sys_info = {
                'timestamp': datetime.now().isoformat(),
                'platform': platform.platform(),
                'machine': platform.machine(),
                'processor': platform.processor(),
                'username': getpass.getuser(),
                'hostname': socket.gethostname(),
                'ip_address': socket.gethostbyname(socket.gethostname()),
                'env_vars': {var: os.environ.get(var, 'N/A') for var in 
                            ['COMPUTERNAME', 'USERNAME', 'USERDOMAIN', 'OS', 'PROCESSOR_ARCHITECTURE']}
            }
            
            # Store encrypted data
            self.store_encrypted_data(sys_info)
            
        except Exception:
            pass
    
    def store_encrypted_data(self, data):
        """Store encrypted system information"""
        try:
            # Generate encryption key
            key = Fernet.generate_key()
            fernet = Fernet(key)
            
            # Convert data to JSON and encrypt
            json_data = json.dumps(data, indent=2)
            encrypted_data = fernet.encrypt(json_data.encode())
            
            # Store in hidden file
            timestamp = str(int(time.time()))
            filename = '.security_assessment_' + timestamp + '.dat'
            file_path = os.path.join(os.getcwd(), filename)
            
            with open(file_path, 'wb') as f:
                f.write(encrypted_data)
            
            # Make file hidden on Windows
            if platform.system().lower() == 'windows':
                try:
                    subprocess.run(['attrib', '+h', '+r', file_path], capture_output=True, timeout=5)
                except:
                    pass
                    
        except Exception:
            pass
    
    def run(self):
        """Run the application"""
        self.root.mainloop()

def main():
    """Main function"""
    app = SecurityAwarenessTool()
    app.run()

if __name__ == "__main__":
    main()
