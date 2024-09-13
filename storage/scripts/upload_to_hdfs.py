from hdfs import InsecureClient

client = InsecureClient('http://localhost:50070', user='root')

def upload_to_hdfs(local_path, hdfs_path):
    client.upload(hdfs_path, local_path)
    print(f"Uploaded {local_path} to {hdfs_path}")

if __name__ == "__main__":
    upload_to_hdfs('data/network_devices.json', '/data/network_devices.json')
