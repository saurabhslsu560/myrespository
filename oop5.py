class resource:
    file=None
    def main():
        try:
            resource.file=open("./bintodec.py")
            print("file opened")
            k=resource.file.read()
            print(k)
        except Exception as msg:
            print("Exception:",msg)
        finally:
            if(resource.file!=None):
                resource.file.close()
            print("file closed")
        return
resource.main()    
