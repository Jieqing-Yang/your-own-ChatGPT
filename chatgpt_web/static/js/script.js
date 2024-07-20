function changeModel(chatUrl) {
    const model = document.getElementById('model').value;
    const url = new URL(chatUrl);
    url.searchParams.set('model', model);
    window.location.href = url;
}

function changeContext(chatUrl) {
    const context = document.getElementById('context').value;
    const url = new URL(chatUrl);
    url.searchParams.set('context', context);
    window.location.href = url;
}

function submitOnEnter(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        event.target.form.submit();
    }
}

function submitForm(event) {
    event.preventDefault();
    event.target.submit();
}
