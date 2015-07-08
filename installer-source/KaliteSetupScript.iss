#define MyAppName "AliuAcademy"
#define MyAppPublisher "Foundation for Learning Equality"
#define MyAppURL "http://learningequality.org/"
#define MyAppExeName "AliuAcademy.exe"

#define getAcademyVersion() \
    Local[1] = Exec(SourcePath+"\getversion.bat") == 0 ? StringChange(FileRead(FileOpen(SourcePath+"\version.temp")), " ", "") : "null"

#define MyVersion = "1.0.0.0"
// getAcademyVersion();

#expr DeleteFile(SourcePath+"\version.temp")

[Setup]
AppId={#MyAppName}-{#MyAppPublisher}
AppName={#MyAppName}
AppVersion={#MyVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
LicenseFile=..\aliuacademy_org\LICENSE
OutputDir=..\
OutputBaseFilename=AliuAcademy-{#MyVersion}
SetupIconFile=logo48.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
UsePreviousAppDir=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "..\aliuacademy_org\*"; DestDir: "{app}\aliuacademy_org"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "..\aliuacademy_org\content\*"; DestDir: "{app}\aliuacademy_org\content"; Flags: ignoreversion recursesubdirs createallsubdirs uninsneveruninstall
Source: "..\aliuacademy_org\academy\database\*"; DestDir: "{app}\aliuacademy_org\academy\database"; Flags: ignoreversion recursesubdirs createallsubdirs uninsneveruninstall
Source: "..\gui-packed\AliuAcademy.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\gui-packed\guitools.vbs"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\gui-packed\images\logo48.ico"; DestDir: "{app}\images"; Flags: ignoreversion
Source: "..\python-setup\*"; DestDir: "{app}\python-setup"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{app}\unins000.exe"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon ; IconFilename: "{app}\images\logo48.ico"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: shellexec postinstall skipifsilent

[Dirs]
Name: "{app}\"; Permissions: everyone-modify


[InstallDelete]
// Type: Files; Name: "{app}\aliuacademy_org\academy\updates\utils.*"

[UninstallDelete]
Type: filesandordirs; Name: "{app}\aliuacademy_org\python-packages"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\base"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\distributed"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\django_cherrypy_wsgiserver"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\login"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\project"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\static"
Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\web"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\khanload"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\loadtesting"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\main"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\management"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\registration"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\securesync"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\shared"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\static"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\templatetags"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\templates"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\tests"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\updates"
// Type: filesandordirs; Name: "{app}\aliuacademy_org\academy\utils"
Type: Files; Name: "{app}\aliuacademy_org\academy\*.pyc"
Type: Files; Name: "{userstartup}\AliuAcademy.lnk"
Type: Files; Name: "{app}\CONFIG.dat"

[Code]
var
  installFlag : boolean;
  startupFlag : string;
  ServerInformationPage : TInputQueryWizardPage;
  UserInformationPage : TInputQueryWizardPage;
  StartupPage : TInputOptionWizardPage;
  existDatabase : boolean;
  isUpgrade : boolean;
  stopServerCode: integer;
  removeOldGuiTool: integer;
  uninstallError: integer;
  saveDatabaseTemp : integer;
  cleanOldAcademyFolder : integer;
  restoreDatabaseTemp : integer;
  forceCancel : boolean;

procedure InitializeWizard;
begin
    existDatabase := False;
    isUpgrade := False;
    forceCancel := False;
    
    if WizardForm.PrevAppDir <> nil then
    begin
        Exec(ExpandConstant('{cmd}'),'/C aliuacademy_org\scripts\stop.bat', WizardForm.PrevAppDir, SW_HIDE, ewWaitUntilTerminated, stopServerCode);
        Exec(ExpandConstant('{cmd}'),'/C del winshortcut.vbs', WizardForm.PrevAppDir, SW_HIDE, ewWaitUntilTerminated, removeOldGuiTool);
    end;
    
    // Server data
    ServerInformationPage := CreateInputQueryPage(wpSelectDir,
    'Server Information', 'General data',
    'Please specify the server name and a description, then click Next. (you can leave blank both fields if you want to use the default server name or if you do not want to insert a description)');
    ServerInformationPage.Add('Server name:', False);
    ServerInformationPage.Add('Server description:', False);
    
    // Admin user creation
    UserInformationPage := CreateInputQueryPage(ServerInformationPage.ID,
    'Admin Information', 'Create admin user',
    'Please specify username and password to create an admin, then click Next.');
    UserInformationPage.Add('Username:', False);
    UserInformationPage.Add('Password:', True);
    UserInformationPage.Add('Confirm Password:', True);
  
    // Run at windows startup.
    StartupPage := CreateInputOptionPage(UserInformationPage.ID,
    'Server Configuration', 'Startup configuration',
    'The server can run automatically. You may choose one of the following options:', True, False);
    StartupPage.Add('Run the server at windows startup');
    StartupPage.Add('Run the server when this user logs in');
    StartupPage.Add('Do not run the server at startup.');
    StartupPage.SelectedValueIndex := 2;
end;

procedure CancelButtonClick(CurPageID: Integer; var Cancel, Confirm: Boolean);
begin
  if forceCancel = True then
  begin
    Confirm := False;
  end;
end;

function ShouldSkipPage(PageID: Integer): Boolean;
begin
    result := False;
    if isUpgrade = True then
    begin
        if PageID = ServerInformationPage.ID then
        begin
            result := True;
        end;
        if PageID = UserInformationPage.ID then
        begin
            result := True;
        end;
        if PageID = wpSelectDir then
        begin
            result := True;
        end;
    end;
end;

procedure HandleExistentDatabase(isOldInstallation : Boolean; targetPath : String);
begin 
    if FileExists(targetPath + '\aliuacademy_org\academy\database\data.sqlite') then
    begin           
        if MsgBox('We have detected an existing AliuAcademy installation; would you like to upgrade?', mbInformation,  MB_YESNO or MB_DEFBUTTON1) = IDYES then
        begin        
            existDatabase := True;
            isUpgrade := True;           
            if isOldInstallation then
            begin
                if Not Exec(ExpandConstant('{cmd}'),'/C ( dir /b "unins***.exe" | findstr /r "unins[0-9][0-9][0-9].exe" ) > tempu & ( for /f "delims=" %A in ( tempu ) do start %A /SILENT /SUPPRESSMSGBOXES ) & del tempu', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, uninstallError) then
                begin
                    Exec(ExpandConstant('{cmd}'),'/C mkdir '+ExpandConstant('{tmp}')+'\aliuacademy_org\academy\database & xcopy /y /s aliuacademy_org\academy\database\data.sqlite '+ExpandConstant('{tmp}')+'\aliuacademy_org\academy\database', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, saveDatabaseTemp);
                    Exec(ExpandConstant('{cmd}'),'/C cd .. & del /q "'+ExpandConstant('{app}')+'\*" & for /d %x in ( "'+ExpandConstant('{app}')+'\*" ) do @rd /s /q "%x"', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, cleanOldAcademyFolder);
                    Exec(ExpandConstant('{cmd}'),'/C mkdir aliuacademy_org\academy\database & xcopy /y /s '+ExpandConstant('{tmp}')+'\aliuacademy_org\academy\database\data.sqlite aliuacademy_org\academy\database', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, restoreDatabaseTemp);
                end;   
            end;           
        end
        else if MsgBox('Installing fresh will delete all of your existing data; is this what you really want to do?', mbInformation,  MB_YESNO or MB_DEFBUTTON2) = IDYES then
        begin
            existDatabase := False;
            isUpgrade := False;
            if Not DeleteFile(targetPath + '\aliuacademy_org\academy\database\data.sqlite') then
            begin
                MsgBox('Error' #13#13 'Failed to delete the old database as requested; aborting the install.', mbError, MB_OK);
                forceCancel := True;
                WizardForm.Close;
            end;
        end
        else
        begin
            existDatabase := True;
            isUpgrade := True;
        end;               
    end;
end;

const
    UCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    LCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz';
    NUMBERS = '1234567890';
    SPECIAL_CHARS = '@.+-_';
    USERNAME_CHARACTERS = UCASE_LETTERS + LCASE_LETTERS + NUMBERS + SPECIAL_CHARS;
    USERNAME_LENGTH = 30; // REF:   https://github.com/learningequality/ka-lite/blob/master/python-packages/django/contrib/auth/models.py#L377
    PASSWORD_LENGTH = 128;  // REF: https://github.com/learningequality/ka-lite/blob/master/python-packages/django/contrib/auth/models.py#L200

function ValidateUserInformationFields(): Boolean;
var
    username : string;
    pass1 : string;
    pass2 : string;
    i: integer;
    s: string;
begin
    result := False;
    // From KA-Lite django.contrib.auth.models.AbstractUser: 
    //   Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters.
    username := UserInformationPage.Values[0];
    pass1 := UserInformationPage.Values[1];
    pass2 := UserInformationPage.Values[2];
    if username <> nil then
    begin
        if (Length(username) > USERNAME_LENGTH) then
        begin
            MsgBox('Error' #13#13 'Username must be at most ' + IntToStr(USERNAME_LENGTH) + ' characters.', mbError, MB_OK);
            result := False;
        end
        else begin
            // check username for valid characters
            for i := 0 to Length(username) do
            begin
                s := Copy(username, i, 1);
                if Pos(s, USERNAME_CHARACTERS) = 0 then
                begin
                     MsgBox('Username must only contain letters, numbers and @/./+/-/_ characters.'#13#13 'It has an invalid character: "' + s + '".', mbError, MB_OK);
                     result := False;
                     exit;
                end;
            end;
            if (pass1 = pass2) And (pass1 <> nil) And (pass2 <> nil) then
            begin
                if Length(pass1) > PASSWORD_LENGTH then
                begin
                    MsgBox('Error' #13#13 'Password must be at most ' + IntToStr(PASSWORD_LENGTH) + ' characters.', mbError, MB_OK);
                    result := False;
                end
                else begin
                    result := True;
                end;
            end
            else begin
                MsgBox('Error' #13#13 'Invalid password or the password does not match on both fields.', mbError, MB_OK);
                result := False;
            end;
        end;
    end
    else begin
        MsgBox('Error' #13#13 'Invalid username. You must enter a non-empty username.', mbError, MB_OK);
        result := False;
    end;
end;

function NextButtonClick(CurPageID: Integer): Boolean;
begin
    result := True;
    
    if CurPageID = UserInformationPage.ID then
    begin
        result := ValidateUserInformationFields();
    end;
    
    if CurPageID = wpLicense then
    begin
        existDatabase := False;
        isUpgrade := False;
        if WizardForm.PrevAppDir <> nil then
        begin
            HandleExistentDatabase(False, WizardForm.PrevAppDir);
        end;
    end;
    
    if CurPageID = wpSelectDir then
    begin
        if Not existDatabase and Not isUpgrade then
        begin
            HandleExistentDatabase(True, ExpandConstant('{app}'));
        end; 
    end;  
end;

procedure HandlePythonSetup;
var
    installPythonErrorCode : Integer;
begin
    if(MsgBox('Install Python?' #13#13 'Python 3.4+ is required to run AliuAcademy; do you wish to first install Python 3.4.3, before continuing with the installation of AliuAcademy?', mbConfirmation, MB_YESNO) = idYes) then
    begin
        ExtractTemporaryFile('python-3.4.3.msi');
        ShellExec('open', ExpandConstant('{tmp}')+'\python-3.4.3.msi', '', '', SW_SHOWNORMAL, ewWaitUntilTerminated, installPythonErrorCode);  
    end
    else begin
        MsgBox('Python Missing' #13#13 'You must have Python 3.4+ installed to proceed! Installation will now exit.', mbError, MB_OK);
        forceCancel := True;
        WizardForm.Close;
    end;
end;

function InitializeSetup(): Boolean;
var
  PythonVersionCodeCheck: integer;
  killErrorCode: integer;
begin
    installFlag:=true;
    Result := true;
    startupFlag:=''; 
  
    ShellExec('open','taskkill.exe','/F /T /im "AliuAcademy.exe"','',SW_HIDE,ewNoWait,killErrorCode)
    ShellExec('open','tskill.exe',' "AliuAcademy"','',SW_HIDE,ewNoWait,killErrorCode);

    RegDeleteValue(HKCU, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Run', ExpandConstant('{#MyAppName}'));
   
    if ShellExec('open', 'python.exe','-c "import sys; sys.version_info[0]==3 and sys.version_info[1] >= 4 and sys.exit(0) or sys.exit(1)"', '', SW_HIDE, ewWaitUntilTerminated, PythonVersionCodeCheck) then
    begin
        if PythonVersionCodeCheck = 1 then
        begin
            HandlePythonSetup();
        end;
    end
    else 
    begin
        HandlePythonSetup();
    end;  
end;

function InitializeUninstall(): Boolean;
var
ErrorCode: Integer;
begin
  ShellExec('open', 'taskkill.exe', '/F /T /im "AliuAcademy.exe"', '', SW_HIDE, ewNoWait, ErrorCode);
  ShellExec('open', 'tskill.exe', '"AliuAcademy"', '', SW_HIDE, ewNoWait, ErrorCode);
  ShellExec('open', ExpandConstant('{app}') + '\aliuacademy_org\stop.bat', '', '', SW_HIDE, ewNoWait, ErrorCode);
  result := True;
end;

procedure CurStepChanged(CurStep: TSetupStep);
var
  ServerNameDescriptionCode: integer;
  StartupCode: integer;
  moveAcademyFolderTemp: integer;
  moveContentFolderTemp: integer;
  cleanAcademyFolder: integer;
  restoreAcademyFolder: integer;
  restoreContentFolder: integer;
  informationBoxFlagged: boolean;
  setupCommand: string;
  
begin
    if CurStep = ssInstall then
    begin
        informationBoxFlagged :=False;
        
        Exec(ExpandConstant('{cmd}'),'/C aliuacademy_org\scripts\stop.bat', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, stopServerCode);
        Exec(ExpandConstant('{cmd}'),'/C del winshortcut.vbs', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, removeOldGuiTool);
    
        if DirExists(ExpandConstant('{app}') + '\academy') then
        begin
            MsgBox('AliuAcademy old data structure' #13#13 'Setup detected that you have the old file structure. Setup will now move data to update the structure. Please be patient; this may take some time.', mbInformation, MB_OK);
            informationBoxFlagged :=True;      
            Exec(ExpandConstant('{cmd}'),'/C mkdir '+ExpandConstant('{tmp}')+'\aliuacademy_org\academy & xcopy /y /s academy\* '+ExpandConstant('{tmp}')+'\aliuacademy_org\academy', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, moveAcademyFolderTemp);      
        end; 
      
        if DirExists(ExpandConstant('{app}') + '\content') then
        begin
            if Not informationBoxFlagged then
            begin
                MsgBox('AliuAcademy old data structure' #13#13 'Setup detected that you have the old file structure. Setup will now move data to update the structure. Please be patient; this may take some time.', mbInformation, MB_OK);
                informationBoxFlagged :=True;
            end;      
            Exec(ExpandConstant('{cmd}'),'/C mkdir '+ExpandConstant('{tmp}')+'\aliuacademy_org\content & xcopy /y /s content\* '+ExpandConstant('{tmp}')+'\aliuacademy_org\content', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, moveContentFolderTemp);      
        end;      
    
        if informationBoxFlagged then
        begin
            Exec(ExpandConstant('{cmd}'),'/C cd .. & del /q "'+ExpandConstant('{app}')+'\*" & for /d %x in ( "'+ExpandConstant('{app}')+'\*" ) do @rd /s /q "%x"', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, cleanAcademyFolder);
    
            if DirExists(ExpandConstant('{tmp}')+'\aliuacademy_org\academy') then
            begin
                Exec(ExpandConstant('{cmd}'),'/C mkdir aliuacademy_org\academy & xcopy /y /s '+ExpandConstant('{tmp}')+'\aliuacademy_org\academy\* aliuacademy_org\academy', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, restoreAcademyFolder);
            end;

            if DirExists(ExpandConstant('{tmp}')+'\aliuacademy_org\content') then
            begin
                Exec(ExpandConstant('{cmd}'),'/C mkdir aliuacademy_org\content & xcopy /y /s '+ExpandConstant('{tmp}')+'\aliuacademy_org\content\* aliuacademy_org\content', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, restoreContentFolder);
            end;
        end;
        
    end;

    if CurStep = ssPostInstall then
    begin
        if installFlag then
        begin
            setupCommand := 'manage.py setup --noinput -o "'+ServerInformationPage.Values[0]+'" -d "'+ServerInformationPage.Values[1]+'" -u "'+UserInformationPage.Values[0]+'" -p "'+UserInformationPage.Values[1]+'"';
            if existDatabase then 
            begin
                setupCommand := setupCommand + ' --noinput';
            end;
            
            MsgBox('Setup will now configure the database. This operation may take a few minutes. Please be patient.', mbInformation, MB_OK);
      
            if Not ShellExec('open', 'python.exe', setupCommand, ExpandConstant('{app}')+'\aliuacademy_org\academy', SW_HIDE, ewWaitUntilTerminated, ServerNameDescriptionCode) then
            begin
                MsgBox('Critical error.' #13#13 'Setup has failed to initialize the database; aborting the install.', mbInformation, MB_OK);
                forceCancel := True;
                WizardForm.Close;
            end;   
      
            if StartupPage.SelectedValueIndex = 0 then
            begin
                if ShellExec('open','guitools.vbs','4', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, StartupCode) then
                begin
                    if Not SaveStringToFile(ExpandConstant('{app}')+'\CONFIG.dat', 'RUN_AT_STARTUP:TRUE;' + #13#10, False) then
                    begin
                        MsgBox('Configuration file error.' #13#13 'Setup has failed to add the entry in the configuration file to run AliuAcademy at Windows startup. The installation may proceed and you can set this option later while using AliuAcademy.', mbError, MB_OK);
                    end;
                end
                else begin
                    MsgBox('GUI tools error.' #13#13 'Setup has failed to register a task to run AliuAcademy at Windows startup. The installation may proceed and you can set this option later while using AliuAcademy.', mbError, MB_OK);
                end;      
            end
            else if StartupPage.SelectedValueIndex = 1 then
            begin
                if ShellExec('open', 'guitools.vbs', '0', ExpandConstant('{app}'), SW_HIDE, ewWaitUntilTerminated, StartupCode) then
                begin
                    if Not SaveStringToFile(ExpandConstant('{app}')+'\CONFIG.dat', 'RUN_AT_USER_LOGIN:TRUE;' + #13#10, False) then
                    begin
                        MsgBox('Configuration file error.' #13#13 'Setup has failed to add the entry in the configuration file to run AliuAcademy on user login. The installation may proceed and you can set this option later while using AliuAcademy.', mbError, MB_OK);
                    end;
                end
                else begin
                    MsgBox('GUI tools error.' #13#13 'Setup has failed to add the shortcut at the startup folder to run AliuAcademy on user login. The installation may proceed and you can set this option later while using AliuAcademy.', mbError, MB_OK);
                end;
            end;
        end;
    end;
    
end;
