import processing


if __name__ == "__main__":
    file_name = "TestData.xlsx"
    proc = processing.ProcessPartA()
    proc.retrieve_data(file_name)
    print('Done')
