function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const darkModeCookie = getCookie('dark_mode');

if (darkModeCookie === 'True') {

    document.body.style.backgroundColor = "#000000";

    const container = document.querySelector('.container');
    if (container) {
        container.style.backgroundColor = "#000000";
    }

    const h1 = document.querySelector('h1');
    h1.style.color = "#e4e4e4"

    const details_p = document.querySelector('details p');
     if (details_p) {
        details_p.style.color = "#e4e4e4"
    }
    

    const back_button = document.querySelector('.back-button');
     if (back_button) {
        back_button.style.color = "#e4e4e4"
    }
    

    const section_h2_all = document.querySelectorAll('.section h2');
    section_h2_all.forEach(h2 => {
        h2.style.color = "#e4e4e4";
    });
    

    const categoryButtons = document.querySelectorAll('.categories button');
    categoryButtons.forEach(button => {
        button.style.color = "#f4f4f4";
    });
}