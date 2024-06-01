import speedtest

def convert_bytes(bytes):
    # Convert bytes to megabytes and gigabytes
    megabytes = bytes / (1024 * 1024)
    gigabytes = megabytes / 1024
    return megabytes, gigabytes

def run_speed_test():
    # Create a Speedtest object
    st = speedtest.Speedtest()

    # Get the download, upload speeds, and ping
    print("Running speed test...")
    print("Testing download speed...")
    download_speed = st.download()
    print("Testing upload speed...")
    upload_speed = st.upload()
    print("Testing ping...")
    ping = st.results.ping

    # Convert speeds to megabytes and gigabytes
    download_mb, download_gb = convert_bytes(download_speed)
    upload_mb, upload_gb = convert_bytes(upload_speed)

    # Print the results
    print(f"Download Speed: {download_mb:.2f} MB/s ({download_gb:.2f} GB/s)")
    print(f"Upload Speed: {upload_mb:.2f} MB/s ({upload_gb:.2f} GB/s)")
    print(f"Ping: {ping:.2f} ms")

# Run the speed test
run_speed_test()
