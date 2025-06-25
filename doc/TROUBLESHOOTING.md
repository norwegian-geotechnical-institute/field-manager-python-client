# Troubleshooting Guide

This guide helps resolve common issues encountered when installing the Field Manager Python Client.

## Windows Long Path Support

**Problem**: Windows users may encounter installation errors due to the 260-character path length limitation:

```
OSError: [Errno 22] Invalid argument: '...'
FileNotFoundError: [Errno 2] No such file or directory
ERROR: Could not install packages due to an EnvironmentError
```

This is particularly common with the field-manager-python-client library due to its nested directory structure.

**Solution**: Enable Windows long path support using PowerShell (requires administrator privileges):

1. **Open PowerShell as Administrator**:
   - Right-click Start button → "Windows PowerShell (Admin)"
   - Or search for PowerShell, right-click, "Run as administrator"

2. **Run the command**:
   ```powershell
   New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
   ```

3. **Restart your computer** for changes to take effect

## Getting Help

If you're still experiencing issues:

1. **Check GitHub Issues**: [field-manager-python-client issues](https://github.com/norwegian-geotechnical-institute/field-manager-python-client/issues)

2. **Create a detailed issue** including:
   - Operating system and version
   - Python version (`python --version`)
   - Complete error message
   - Steps to reproduce the problem

## Frequently Asked Questions
