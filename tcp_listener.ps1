# Define the TCP port number to listen on
$port = 515  # Replace with your desired port number

# Create a listener on the specified port
$listener = [System.Net.Sockets.TcpListener]$port
$listener.Start()

Write-Host "Listening on port $port..."

# Accept an incoming connection
$client = $listener.AcceptTcpClient()
$stream = $client.GetStream()

$reader = New-Object System.IO.StreamReader($stream)
$writer = New-Object System.IO.StreamWriter($stream)
$writer.AutoFlush = $true

# Read and print data from the client
while ($stream.DataAvailable) {
    $line = $reader.ReadLine()
    Write-Host "Received: $line"
}

# Clean up
$reader.Close()
$writer.Close()
$stream.Close()
$client.Close()
$listener.Stop()

Write-Host "Connection closed."
