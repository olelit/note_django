let addNoteModal = document.querySelector('.add_notify'),
    createNotifyModal = document.querySelector('.create_notify'),
    close = document.querySelectorAll('.close'),
    data_item = document.querySelectorAll('.data_item'),
    sort = document.querySelector('#sort_option');

if (addNoteModal) {
    addNoteModal.addEventListener('click', (event) => {
        let forSelector = event.currentTarget.dataset.for;
        document.querySelector(forSelector).classList.remove('hide');
    });
}

if(sort){
    document.querySelector('#sort_form').submit();
}

if (data_item) {
    data_item.forEach((item) => {
        item.addEventListener('click', (event) => {
            let id = event.currentTarget.dataset.id;
            axios.post('/get/note/', {
                id: id,
            }, {
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                    "content-type": "application/json"
                }
            })
                .then((response) => {
                    document.querySelector('#note_content .modal_content').innerHTML = response['data'];
                    document.querySelector('#note_content').classList.remove('hide');
                }, (error) => {
                    console.log(error);
                });
        })
    });
}

if (close) {
    close.forEach((button) => {
        button.addEventListener('click', (event) => {
            let wrapper = event.currentTarget.closest('.modal_wrapper');
            wrapper.classList.add('hide');
        })
    });
}
