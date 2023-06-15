from butler import Client

# Specify variables for use in script below
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTg3MDY0MjgxMzEyMDI5MTU3MCIsImVtYWlsIjoibWlyYWNsZTM0OTgyMUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaWF0IjoxNjg2MjA2MzgyNjI2fQ.ClBvcbwrXr_rAqTiPsMUwAwSZJNUpSEzyTMVlAdofRI'
queue_id = 'd407d57a-301d-4a4d-957c-5222b3d31021'

# Specify the path to the file you would like to process
file_location = '/path/to/file'

response = Client(api_key).extract_document(queue_id, file_location)
print(response)