<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Hugo 0.84.0">
    <title>SecurePark</title>
    <link rel="shortcut icon" href="/img/logo.png" type="image/x-icon">

    <!-- Bootstrap core CSS -->
    <link href="/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="navbar-top-fixed.css" rel="stylesheet">
    <link rel="stylesheet" href="/css/park.css">

    <!-- Firebase SDK -->
    <script src="https://www.gstatic.com/firebasejs/8.6.8/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/8.6.8/firebase-database.js"></script>
</head>
<body>
    <section class="element">
        <nav class="navbar navbar-expand-md navbar fixed-top">
            <div class="container-fluid">
                <a class="navbar-brand" href="/" style="">
                    <img class="logo" src="/img/logo.png" style="">
                    <b>SecurePark</b>
                </a>
            </div>
        </nav>

        <!--MAIN-->
        <main class="container border border-5 area-park" style="margin-top:70px">
            <div class="row justify-content-center align-items-center">
                <div class="col-auto text-center d-flex align-items-center">
                    <p class="entrance-text">Pintu Masuk</p>
                    <img class="gate" src="/img/ko.png" alt="Gate In">
                </div>
                <div class="col">
                    <div class="row justify-content-center">
                        <img class="kotak slot" src="/img/1.png" data-slot-id="1">
                        <img class="kotak slot" src="/img/2.png" data-slot-i
                        7="2">
                        <img class="kotak slot" src="/img/3.png" data-slot-id="3">
                        <img class="kotak slot" src="/img/4.png" data-slot-id="4">
                        <img class="kotak slot" src="/img/5.png" data-slot-id="5">
                    </div>
                    <!-- Add jalan image here -->
                    <div class="row kotak-bawah justify-content-center">
                        <img class="jalan" src="/img/pa.png" alt="Jalan">
                    </div>
                    <div class="row kotak-bawah justify-content-center">
                        <img class="kotak slot" src="/img/6.png" data-slot-id="6">
                        <img class="kotak slot" src="/img/7.png" data-slot-id="7">
                        <img class="kotak slot" src="/img/8.png" data-slot-id="8">
                        <img class="kotak slot" src="/img/9.png" data-slot-id="9">
                        <img class="kotak slot" src="/img/10.png" data-slot-id="10">
                    </div>
                </div>
                <div class="col-auto text-center d-flex align-items-center">
                    <img class="barrier" src="/img/lo.png" alt="Exit Barrier">
                    <p class="exit-text">Pintu Keluar</p>

                </div>
            </div>
        </main>
        <footer class="container ket-bawah">
            <div class="row justify-content-center">
                <div class="col-3 tersedia text-center p-3"><b>TERSEDIA</b></div>
                <div class="col-3 terisi text-center p-3"><b>TERISI</b></div>
            </div>
        </footer>
    </section>
    <div class="container">
        <div class="d-flex justify-content-end">
            <button type="button" class="toggle btn btn-info">Fullscreen</button>
        </div>
    </div>

    <script src="/js/bootstrap.bundle.min.js"></script>
    <script src="/js/park.js"></script>
</body>
</html>
