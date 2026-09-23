from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, file_name, data):
        pass

    @abstractmethod
    def download_file(self, file_name):
        pass

    @abstractmethod
    def delete_file(self, file_name):
        pass

class AWSS3Storage(CloudStorage):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def upload_file(self, file_name, data):
        return f"Uploaded '{file_name}' to AWS S3 bucket '{self.bucket_name}'."

    def download_file(self, file_name):
        return f"Downloaded '{file_name}' from AWS S3 bucket '{self.bucket_name}'."

    def delete_file(self, file_name):
        return f"Deleted '{file_name}' from AWS S3 bucket '{self.bucket_name}'."

class GoogleCloudStorage(CloudStorage):
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def upload_file(self, file_name, data):
        return f"Uploaded '{file_name}' to Google Cloud Storage bucket '{self.bucket_name}'."

    def download_file(self, file_name):
        return f"Downloaded '{file_name}' from Google Cloud Storage bucket '{self.bucket_name}'."

    def delete_file(self, file_name):
        return f"Deleted '{file_name}' from Google Cloud Storage bucket '{self.bucket_name}'."

class AzureBlobStorage(CloudStorage):
    def __init__(self, container_name):
        self.container_name = container_name

    def upload_file(self, file_name, data):
        return f"Uploaded '{file_name}' to Azure Blob container '{self.container_name}'."

    def download_file(self, file_name):
        return f"Downloaded '{file_name}' from Azure Blob container '{self.container_name}'."

    def delete_file(self, file_name):
        return f"Deleted '{file_name}' from Azure Blob container '{self.container_name}'."

if __name__ == "__main__":
    storage_providers = [
        AWSS3Storage("company-aws-bucket"),
        GoogleCloudStorage("company-gcp-bucket"),
        AzureBlobStorage("company-azure-container")
    ]

    filename = "report.pdf"
    file_data = "sample_binary_content"

    for provider in storage_providers:
        print(f"=== {type(provider).__name__} ===")
        print(provider.upload_file(filename, file_data))
        print(provider.download_file(filename))
        print(provider.delete_file(filename))
        print()
