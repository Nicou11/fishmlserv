# fishmlserv

## fastapi Creating

### Deploy
![image](https://github.com/user-attachments/assets/a2665a21-109f-415b-a974-06495ce8d23d)


### Run
- dev
- http://localhost:8000/docs
```bash
# uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```
- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```

### Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```

### Ref
- https://curlconverter.com/python
