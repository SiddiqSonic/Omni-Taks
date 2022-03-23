console.log("Hello world");

const url = window.location.href;
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultbox = document.getElementById('resultbox');
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
// const csrf = document.querySelector('name="csrfmiddlewaretoken"').value;
// console.log(csrf);


const sendSearchData = (searchKeyWord) => {
    $.ajax({
        type: 'POST',
        url: 'listing/search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'searchKeyWord': searchKeyWord
        },
        success: (res) => {
            resultbox.innerHTML = "";
            // console.log(res);
            const data = res.data;
            if (Array.isArray(data)) {
                resultbox.classList.remove("Hide");
                data.forEach(movie => {
                    const p = document.createElement('p');
                    p.innerHTML = "<a href = 'http://127.0.0.1:8000/listing/" + movie.id + "'>" + movie.name + "</a>";
                    resultbox.append(p);
                    // console.log(movie);
                });

            } else {
                if (searchInput.value.length > 0) {
                    resultbox.classList.remove("Hide");
                    resultbox.innerHTML = "<br>" + data + "</br>"
                } else {
                    resultbox.classList.add("Hide");
                    resultbox.innerHTML = "";
                }
            }
        },
        error: (err) => {

            console.log(err);
        }
    })
}

searchInput.addEventListener('keyup', e => {
    // console.log(e.target.value);
    sendSearchData(e.target.value);
})