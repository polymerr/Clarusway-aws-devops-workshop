FROM python:alpine
COPY . /app                  # Hangi klasördeysen o klasördekileri image'ın içine atıyor
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 80                       # expose etmek konteynerin hangi porttan run edilmesi demektir.
CMD ["python", "bookstore-api.py"]        # CMD ne olduğunu konu anlatımında bakarsın, kaçırdım çünkü
