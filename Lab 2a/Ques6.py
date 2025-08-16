def extsort(file_list):
    """
    Sorts a list of filenames by their extension.
    If two files have the same extension, they are sorted by filename.

    Args:
        file_list (list[str]): List of filenames

    Returns:
        list[str]: Sorted list of filenames
    """
    return sorted(file_list, key=lambda x: (x.split('.')[-1], x.split('.')[0]))


# Driver code to test above
arr = ["doc1.docx","file1.txt", "ppt1.pptx","file3.txt","img2.jpg", "file4.txt", "img1.png", "file2.txt", "doc2.docx","ppt2.pptx"]
n = len(arr)
print("Given array is")
for i in range(n):
    print("%s" % arr[i],end=" ")

arr = extsort(arr)
print("\nSorted array is")
for i in range(n):
    print("%s" % arr[i],end=" ")