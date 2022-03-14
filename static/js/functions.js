// document.addEventListener('scroll', function(e) {
//             if (window.scrollY > window.innerHeight) {
//                 var currScrollPos2 = window.scrollY;
//                 document.getElementById('header').style.opacity = 4*((-window.innerHeight/currScrollPos2)+1);
//                 }
//             });

document.addEventListener('scroll', function(e) {
            if (window.scrollY > window.innerHeight) {
                document.getElementById('header').style.display = "block";
                }
            });