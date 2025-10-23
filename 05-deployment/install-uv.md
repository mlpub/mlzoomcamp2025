# Install uv

## Install in Ubuntu 22.04

Update Ubuntu.
```
sudo apt update
sudo apt upgrade
```

Open terminal and run install script ( copy from https://docs.astral.sh/uv/#highlights ).
```
curl -LsSf https://astral.sh/uv/install.sh | sh
``` 
When install success, the output should likes:
```
downloading uv 0.9.5 x86_64-unknown-linux-gnu
no checksums to verify
installing to /home/minipc/.local/bin
  uv
  uvx
everything's installed!
```

Close the terminal and reopen again, to take effect. Than check uv by run:
```
uv --version
```
The output should likes:
```
uv 0.9.5
```


## Install in Windows

Open Windows PowerShell, and run:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

When install success, the output should likes:
```
Installing to C:\Users\demo\.local\bin
  uv.exe
  uvx.exe
  uvw.exe
everything's installed!
```

Close the PowerShell and reopen again, run:
```
uv --version
```
The output should likes:
```
uv 0.9.5 (d5f39331a 2025-10-21)
```

