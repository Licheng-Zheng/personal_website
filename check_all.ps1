$htmlFiles = @("index.html", "projects.html") + (Get-ChildItem "project_pages\*.html").FullName

foreach ($file in $htmlFiles) {
    if (-not (Test-Path $file)) { continue }
    $content = Get-Content $file -Raw
    
    # Match src=""
    $matches = [regex]::Matches($content, 'src=["''](.*?)["'']')
    foreach ($match in $matches) {
        $link = $match.Groups[1].Value
        
        # Check if external
        if ($link -match "^http") {
            try {
                $response = Invoke-WebRequest -Uri $link -UseBasicParsing -Method Head -ErrorAction Stop
            } catch {
                Write-Host "External Broken: $link in $file"
            }
            continue
        }

        # Ignore data URI
        if ($link -match "^data:") { continue }

        $cleanLink = $link -replace '#.*$', '' -replace '\?.*$', ''
        if ($cleanLink -eq "") { continue }

        $dir = Split-Path $file
        if ($dir -eq "") { $dir = "." }
        $target = [System.IO.Path]::GetFullPath((Join-Path $dir $cleanLink))
        
        if (-not (Test-Path $target)) {
            Write-Host "Local Missing src: $cleanLink in $file"
        }
    }
    
    # Match css url(...)
    $urlMatches = [regex]::Matches($content, 'url\((?:["'']?)(.*?)(?:["'']?)\)')
    foreach ($match in $urlMatches) {
        $link = $match.Groups[1].Value
        if ($link -match "^http" -or $link -match "^data:") { continue }
        
        $cleanLink = $link -replace '#.*$', '' -replace '\?.*$', ''
        if ($cleanLink -eq "") { continue }

        $dir = Split-Path $file
        if ($dir -eq "") { $dir = "." }
        $target = [System.IO.Path]::GetFullPath((Join-Path $dir $cleanLink))
        
        if (-not (Test-Path $target)) {
            Write-Host "Local Missing CSS url: $cleanLink in $file"
        }
    }
}
Write-Host "Done checking!"
