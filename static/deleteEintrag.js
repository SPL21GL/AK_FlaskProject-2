function deleteGast(element) {
    if(window.confirm("Wollen Sie diesen Gast wirklich löschen"))
    {
        element.parentElement.submit();
    }
}

function deleteAbendveranstaltungen(element) {
    if(window.confirm("Wollen Sie diese Abendveranstaltung wirklich löschen"))
    {
        element.parentElement.submit();
    }
}


function deleteReservationsmitarbeiter(element) {
    if(window.confirm("Wollen Sie diesen Mitarbeiter wirklich löschen"))
    {
        element.parentElement.submit();
    }
}

/* 
document.querySelector("a[href='/products']").classList.add("active")
*/