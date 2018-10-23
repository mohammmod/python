# docker with python script.

<ul>
<li> create ur python script first .
<li> write your docker file as 
  <ol>
    <li>FROM python:3
    <li>ADD your_script.py /
    <li>RUN pip install pystrich
    <li>CMD [ "python", "./your_script.py" ] 
  </ol>
<li> run the command `docker build . -t image-name` example :`docker build . -t hello`
<li> run the image using `docker run image name`
</ul>
