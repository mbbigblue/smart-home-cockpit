class FileCreator:

    def generate_filename(file_path):
        """
        Generates a name for the supplied MatrixStore file which includes various
        details about it

        The name is structured so that sorting lexically gives the file with the
        latest build of the latest data. It includes a hash of the file's contents
        which can be used as a cache key and also for de-duplication (so it's easy
        to see if rebuilding a file has resulted in any change to the data).
        """
        last_modified = datetime.datetime.utcfromtimestamp(os.path.getmtime(file_path))
        max_date = get_max_date_from_file(file_path)
        hash_str = hash_file(file_path)
        return "matrixstore_{max_date}_{modified}_{hash}.sqlite".format(
            max_date=max_date.strftime("%Y-%m"),
            modified=last_modified.strftime("%Y-%m-%d--%H-%M"),
            hash=hash_str[:16],
        )