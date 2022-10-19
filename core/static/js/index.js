// $(document).ready(function () {
//     $("#search_filter").on("keyup", function () {
//         var value = $(this).val().toLowerCase();
//         $(".container_ div").filter(function () {
//             $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
//         })
//     })
// })


// const search = () => {
//     const searchbox = document.getElementById('search_filter').value.toUpperCase();
//     const items = document.getElementsByClassName("container_")
//     const item = document.querySelectorAll('.box')
//     const itemName = items.getElementsByTagName('h6')

//     for (var i = 0; i < itemName.length; i++) {
//         let match = item[i].getElementsByTagName('h6')[0];

//         if (match) {
//             let textValue = match.textContent || match.innerHTML

//             if (textValue.toUpperCase().indexOf(searchbox) > -1) {
//                 item[i].style.display = "";
//             } else {
//                 item[i].style.display = "none";
//             }

//         }
//     }
// }