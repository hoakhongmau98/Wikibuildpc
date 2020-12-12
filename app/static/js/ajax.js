// document.addEventListener('DOMContentLoaded', (event) => {
//     $(".call_object").dblclick(function () {
//         var call_arg = $(this).val();
//         $.ajax({
//             url: "/call_prodcut",
//             type: "get",
//             data: {call_arg: call_arg},
//
//             success: function (response) {
//                 $(".build_product").html(response);
//             },
//             error: function (xhr) {
//                 //Do Something to handle error
//             }
//         });
//     });
//     $(".call_object").dblclick(function () {
//         var call_arg = $(this).val();
//         $.ajax({
//             url: "/categories",
//             type: "get",
//             data: {call_arg: call_arg},
//
//             success: function (response) {
//                 $(".categories").html(response);
//             },
//             error: function (xhr) {
//                 //Do Something to handle error
//             }
//         });
//     });
// })