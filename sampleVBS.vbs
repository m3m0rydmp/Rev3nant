' VBScript GUI Example for Security Awareness Testing
' Creates a simple dialog box that looks like a system update

Set objIE = CreateObject("InternetExplorer.Application")

' Configure IE window
objIE.Navigate "about:blank"
objIE.ToolBar = False
objIE.StatusBar = False
objIE.Width = 400
objIE.Height = 300
objIE.Left = 100
objIE.Top = 100
objIE.Resizable = False
objIE.Visible = True

' Wait for page to load
Do While objIE.Busy
    WScript.Sleep 100
Loop

' Create custom HTML content
strHTML = "<html><head><title>System Update</title>" & _
          "<style>body{font-family:Arial;background:#f0f0f0;margin:20px;}" & _
          "h2{color:#0066cc;margin-bottom:20px;}" & _
          ".button{padding:8px 16px;background:#0066cc;color:white;border:none;cursor:pointer;}" & _
          "</style></head><body>" & _
          "<h2>Windows Security Update</h2>" & _
          "<p>A critical security update is available for your system.</p>" & _
          "<p>Click 'Install Now' to proceed with the installation.</p>" & _
          "<button class='button' onclick='alert(""Security Awareness Test - You clicked the button!"");window.close();'>Install Now</button>" & _
          "<button class='button' onclick='window.close();' style='margin-left:10px;background:#666;'>Cancel</button>" & _
          "</body></html>"

objIE.Document.Write strHTML

' Alternative simple message box approach
' MsgBox "This is a security awareness test!" & vbCrLf & "You opened a file from an unknown USB drive.", vbExclamation, "Security Alert"

' Keep window open until closed by user
Do While Not objIE.Document.readyState = "complete"
    WScript.Sleep 100
Loop