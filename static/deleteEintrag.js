function deleteEntry(element) {

    if(window.confirm("Wollen Sie den Eintrag wirklich löschen"))
    {
        element.parentElement.submit();
    }

}