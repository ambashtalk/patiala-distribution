function validate_me(){
    document.getElementById("key").addEventListener("keypress", function (e) {
        console.log(e);
        if ((e.charCode >= 65 && e.charCode <= 90)||(e.charCode >= 97 && e.charCode <= 122))
            {

            }
        else {
            e.preventDefault();
        }
        return false;
    });
}