def upload_file_to_s3(
    client: "Client", file: Dict[str, Any], file_path: Path, team: str
) -> requests.Response:
    """Helper function: upload data to AWS S3

    Parameters
    ----------
    client: Client
        Client to use to authenticate the upload
    file: dict
        The file as a response from the client.put() operation
    file_path: Path
        Path to the file to upload on the file system

    Returns
    -------
    requests.Response
        s3 response
    """
    key = file["key"]
    image_id = file["id"]
    response = sign_upload(client, image_id, key, file_path, team)
    signature = response["signature"]
    end_point = response["postEndpoint"]
    return requests.post("http:" + end_point, data=signature, files={"file": file_path.open("rb")})