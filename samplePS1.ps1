# Advanced PowerShell GUI for Security Testing
# Modern Windows 10/11 style interface

Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create main form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Microsoft Security Essentials"
$form.Size = New-Object System.Drawing.Size(600,450)
$form.StartPosition = "CenterScreen"
$form.FormBorderStyle = "FixedDialog"
$form.MaximizeBox = $false
$form.BackColor = [System.Drawing.Color]::White

# Create header panel
$headerPanel = New-Object System.Windows.Forms.Panel
$headerPanel.Size = New-Object System.Drawing.Size(584,80)
$headerPanel.Location = New-Object System.Drawing.Point(0,0)
$headerPanel.BackColor = [System.Drawing.Color]::FromArgb(0,120,215)
$form.Controls.Add($headerPanel)

# Header icon (simulated)
$iconLabel = New-Object System.Windows.Forms.Label
$iconLabel.Text = "🛡️"
$iconLabel.Font = New-Object System.Drawing.Font("Segoe UI Emoji",20)
$iconLabel.ForeColor = [System.Drawing.Color]::White
$iconLabel.Location = New-Object System.Drawing.Point(20,25)
$iconLabel.Size = New-Object System.Drawing.Size(40,30)
$headerPanel.Controls.Add($iconLabel)

# Header title
$headerTitle = New-Object System.Windows.Forms.Label
$headerTitle.Text = "Microsoft Security Essentials"
$headerTitle.Font = New-Object System.Drawing.Font("Segoe UI",16,[System.Drawing.FontStyle]::Bold)
$headerTitle.ForeColor = [System.Drawing.Color]::White
$headerTitle.Location = New-Object System.Drawing.Point(70,20)
$headerTitle.Size = New-Object System.Drawing.Size(400,25)
$headerPanel.Controls.Add($headerTitle)

# Header subtitle
$headerSubtitle = New-Object System.Windows.Forms.Label
$headerSubtitle.Text = "Real-time protection for your PC"
$headerSubtitle.Font = New-Object System.Drawing.Font("Segoe UI",9)
$headerSubtitle.ForeColor = [System.Drawing.Color]::LightBlue
$headerSubtitle.Location = New-Object System.Drawing.Point(70,45)
$headerSubtitle.Size = New-Object System.Drawing.Size(300,20)
$headerPanel.Controls.Add($headerSubtitle)

# Main content area
$mainPanel = New-Object System.Windows.Forms.Panel
$mainPanel.Location = New-Object System.Drawing.Point(20,100)
$mainPanel.Size = New-Object System.Drawing.Size(540,300)
$mainPanel.BackColor = [System.Drawing.Color]::White
$form.Controls.Add($mainPanel)

# Status section
$statusLabel = New-Object System.Windows.Forms.Label
$statusLabel.Text = "Protection Status"
$statusLabel.Font = New-Object System.Drawing.Font("Segoe UI",12,[System.Drawing.FontStyle]::Bold)
$statusLabel.Location = New-Object System.Drawing.Point(0,10)
$statusLabel.Size = New-Object System.Drawing.Size(200,25)
$mainPanel.Controls.Add($statusLabel)

# Warning panel
$warningPanel = New-Object System.Windows.Forms.Panel
$warningPanel.Location = New-Object System.Drawing.Point(0,40)
$warningPanel.Size = New-Object System.Drawing.Size(540,60)
$warningPanel.BackColor = [System.Drawing.Color]::FromArgb(255,243,205)
$warningPanel.BorderStyle = "FixedSingle"
$mainPanel.Controls.Add($warningPanel)

$warningIcon = New-Object System.Windows.Forms.Label
$warningIcon.Text = "⚠️"
$warningIcon.Font = New-Object System.Drawing.Font("Segoe UI Emoji",16)
$warningIcon.Location = New-Object System.Drawing.Point(15,15)
$warningIcon.Size = New-Object System.Drawing.Size(30,30)
$warningPanel.Controls.Add($warningIcon)

$warningText = New-Object System.Windows.Forms.Label
$warningText.Text = "Potential threats detected from external USB device"
$warningText.Font = New-Object System.Drawing.Font("Segoe UI",10,[System.Drawing.FontStyle]::Bold)
$warningText.ForeColor = [System.Drawing.Color]::FromArgb(133,100,4)
$warningText.Location = New-Object System.Drawing.Point(50,10)
$warningText.Size = New-Object System.Drawing.Size(450,20)
$warningPanel.Controls.Add($warningText)

$warningSubtext = New-Object System.Windows.Forms.Label
$warningSubtext.Text = "A full system scan is recommended to ensure your safety"
$warningSubtext.Font = New-Object System.Drawing.Font("Segoe UI",9)
$warningSubtext.ForeColor = [System.Drawing.Color]::FromArgb(133,100,4)
$warningSubtext.Location = New-Object System.Drawing.Point(50,30)
$warningSubtext.Size = New-Object System.Drawing.Size(450,20)
$warningPanel.Controls.Add($warningSubtext)

# Scan options
$scanLabel = New-Object System.Windows.Forms.Label
$scanLabel.Text = "Recommended Action"
$scanLabel.Font = New-Object System.Drawing.Font("Segoe UI",12,[System.Drawing.FontStyle]::Bold)
$scanLabel.Location = New-Object System.Drawing.Point(0,120)
$scanLabel.Size = New-Object System.Drawing.Size(200,25)
$mainPanel.Controls.Add($scanLabel)

# Progress bar
$progressBar = New-Object System.Windows.Forms.ProgressBar
$progressBar.Location = New-Object System.Drawing.Point(0,200)
$progressBar.Size = New-Object System.Drawing.Size(540,25)
$progressBar.Style = "Continuous"
$progressBar.Value = 0
$mainPanel.Controls.Add($progressBar)

# Progress label
$progressLabel = New-Object System.Windows.Forms.Label
$progressLabel.Text = "Click 'Scan Now' to begin security scan"
$progressLabel.Font = New-Object System.Drawing.Font("Segoe UI",9)
$progressLabel.Location = New-Object System.Drawing.Point(0,175)
$progressLabel.Size = New-Object System.Drawing.Size(540,20)
$mainPanel.Controls.Add($progressLabel)

# Scan details
$detailsLabel = New-Object System.Windows.Forms.Label
$detailsLabel.Text = "Scan Details:"
$detailsLabel.Font = New-Object System.Drawing.Font("Segoe UI",9,[System.Drawing.FontStyle]::Bold)
$detailsLabel.Location = New-Object System.Drawing.Point(0,235)
$detailsLabel.Size = New-Object System.Drawing.Size(100,20)
$mainPanel.Controls.Add($detailsLabel)

$detailsText = New-Object System.Windows.Forms.TextBox
$detailsText.Location = New-Object System.Drawing.Point(0,255)
$detailsText.Size = New-Object System.Drawing.Size(540,40)
$detailsText.Multiline = $true
$detailsText.ScrollBars = "Vertical"
$detailsText.ReadOnly = $true
$detailsText.Text = "Ready to scan for potential security threats..."
$detailsText.Font = New-Object System.Drawing.Font("Consolas",8)
$mainPanel.Controls.Add($detailsText)

# Button panel
$buttonPanel = New-Object System.Windows.Forms.Panel
$buttonPanel.Location = New-Object System.Drawing.Point(20,360)
$buttonPanel.Size = New-Object System.Drawing.Size(540,50)
$form.Controls.Add($buttonPanel)

# Scan Now button
$scanButton = New-Object System.Windows.Forms.Button
$scanButton.Text = "Scan Now"
$scanButton.Font = New-Object System.Drawing.Font("Segoe UI",10,[System.Drawing.FontStyle]::Bold)
$scanButton.Size = New-Object System.Drawing.Size(120,35)
$scanButton.Location = New-Object System.Drawing.Point(150,10)
$scanButton.BackColor = [System.Drawing.Color]::FromArgb(0,120,215)
$scanButton.ForeColor = [System.Drawing.Color]::White
$scanButton.FlatStyle = "Flat"
$buttonPanel.Controls.Add($scanButton)

# Quick Scan button
$quickButton = New-Object System.Windows.Forms.Button
$quickButton.Text = "Quick Scan"
$quickButton.Font = New-Object System.Drawing.Font("Segoe UI",9)
$quickButton.Size = New-Object System.Drawing.Size(100,35)
$quickButton.Location = New-Object System.Drawing.Point(280,10)
$quickButton.BackColor = [System.Drawing.Color]::FromArgb(108,117,125)
$quickButton.ForeColor = [System.Drawing.Color]::White
$quickButton.FlatStyle = "Flat"
$buttonPanel.Controls.Add($quickButton)

# Cancel button
$cancelButton = New-Object System.Windows.Forms.Button
$cancelButton.Text = "Later"
$cancelButton.Font = New-Object System.Drawing.Font("Segoe UI",9)
$cancelButton.Size = New-Object System.Drawing.Size(80,35)
$cancelButton.Location = New-Object System.Drawing.Point(390,10)
$cancelButton.BackColor = [System.Drawing.Color]::FromArgb(220,53,69)
$cancelButton.ForeColor = [System.Drawing.Color]::White
$cancelButton.FlatStyle = "Flat"
$buttonPanel.Controls.Add($cancelButton)

# Scan function
function Start-SecurityScan {
    $scanButton.Enabled = $false
    $quickButton.Enabled = $false
    
    $scanSteps = @(
        "Initializing security scanner...",
        "Loading virus definitions...",
        "Scanning system memory...",
        "Checking running processes...",
        "Scanning external devices...",
        "Analyzing suspicious files...",
        "Checking network connections...",
        "Finalizing scan results..."
    )
    
    $detailsText.Text = ""
    
    for ($i = 0; $i -lt $scanSteps.Length; $i++) {
        $progressLabel.Text = $scanSteps[$i]
        $detailsText.AppendText("$(Get-Date -Format 'HH:mm:ss') - $($scanSteps[$i])`r`n")
        
        for ($j = 0; $j -le 12; $j++) {
            $progressValue = [math]::Round((($i * 12 + $j) / ($scanSteps.Length * 12)) * 100)
            $progressBar.Value = $progressValue
            Start-Sleep -Milliseconds 100
            [System.Windows.Forms.Application]::DoEvents()
        }
    }
    
    $progressBar.Value = 100
    $progressLabel.Text = "Scan completed successfully"
    
    # Show security awareness message
    [System.Windows.Forms.MessageBox]::Show(
        "🎯 SECURITY AWARENESS TEST COMPLETE! 🎯`n`n" +
        "This was a simulated social engineering attack!`n`n" +
        "You just executed a program from an untrusted USB device. In a real attack, this could have:`n`n" +
        "• Installed malware or ransomware`n" +
        "• Stolen your credentials and sensitive data`n" +
        "• Given attackers remote access to your system`n" +
        "• Compromised your entire network`n`n" +
        "🛡️ Security Best Practices:`n" +
        "• Never plug in unknown USB devices`n" +
        "• Scan all external media before use`n" +
        "• Be suspicious of unexpected security alerts`n" +
        "• Always verify with IT before running unknown programs`n`n" +
        "Thank you for participating in this security exercise!",
        "Security Awareness Training",
        "OK",
        "Information"
    )
    
    $form.Close()
}

# Quick scan function
function Start-QuickScan {
    $scanButton.Enabled = $false
    $quickButton.Enabled = $false
    $progressLabel.Text = "Running quick security scan..."
    
    for ($i = 0; $i -le 100; $i++) {
        $progressBar.Value = $i
        Start-Sleep -Milliseconds 50
        [System.Windows.Forms.Application]::DoEvents()
    }
    
    Start-SecurityScan
}

# Event handlers
$scanButton.Add_Click({ Start-SecurityScan })
$quickButton.Add_Click({ Start-QuickScan })
$cancelButton.Add_Click({
    $result = [System.Windows.Forms.MessageBox]::Show(
        "Are you sure you want to postpone the security scan?`n`nYour system may remain vulnerable to threats.",
        "Postpone Scan",
        "YesNo",
        "Warning"
    )
    if ($result -eq "Yes") {
        Start-SecurityScan
    }
})

# Show the form
$form.ShowDialog()