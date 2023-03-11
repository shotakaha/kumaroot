# チュートリアル

```bash
$ docker run --name repo alpine/git clone https://github.com/docker/getting-started.git
$ docker cp repo:/git/getting-started/ .

Unable to find image 'alpine/git:latest' locally
latest: Pulling from alpine/git
6875df1f5354: Pull complete
1eb88bc83e71: Pull complete
0a50dc9da39b: Pull complete
Digest: sha256:66b210a97bc07bfd4019826bcd13a488b371a6cbe2630a4b37d23275658bd3f2
Status: Downloaded newer image for alpine/git:latest
Cloning into 'getting-started'...

$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
alpine/git   latest    9793ee61fc75   3 months ago   43.4MB

$ docker container ls
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

$ cd getting-started
$ docker build -t docker101tutorial .
[+] Building 27.2s (27/27) FINISHED
(...省略...)
=> exporting to image                                0.0s
=> => exporting layers                               0.0s
=> => writing image sha256:94a1f545e696719558fe2bfa  0.0s
=> => naming to docker.io/library/docker101tutorial  0.0s

$ docker image
REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
docker101tutorial   latest    94a1f545e696   25 seconds ago   46.5MB
alpine/git          latest    9793ee61fc75   3 months ago     43.4MB

$ docker run -d -p 80:80 --name docker-tutorial docker101tutorial
6fd342210287e029fbe9bcefdaf4e650c9a7ae57f0c12b824508683740e11386

$ docker container ls
CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS          PORTS                NAMES
6fd342210287   docker101tutorial   "/docker-entrypoint.…"   22 seconds ago   Up 21 seconds   0.0.0.0:80->80/tcp   docker-tutorial
```
