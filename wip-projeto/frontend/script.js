// funções de catch dos dados
async function buscarTodasMensagens() {
    try {
        const response = await fetch(`http://localhost:5000`, {
            headers: { 'Content-Type': 'application/json' },
            method: "GET"
        });

        if (!response.ok) {
            throw new error("Could not fetch resource!");
        }
        const data = await response.json(); 
        if (data.length == 0) {
            tabelaVazia()
        } else {
            incluirTabela(data);            
        }  
    }
    catch (error) {
        tabelaVazia()
        console.log(error);
    }
}

// mostrar div aviso tabela vazia ou sem conexção DB
function tabelaVazia() {
    $('.head-tabela').remove();
    $('.linha_dinamica').remove();
    $('.mensagem-erro').remove();
    $(".no-files").append(`<p class='mensagem-erro'>Tabela vazia. Favor verificar se há comunicação com o Banco de Dados.</p>`)
}

// mostrar dados tabela
function incluirTabela(data) {
    $('.head-tabela').remove()
    $('.mensagem-erro').remove()
    $('#tabela').append(
        `
        <tr class='head-tabela'>
                <th>n°</th>
                <th>id_mensagem</th>
                <th>id_user</th>
                <th>first_name</th>
                <th>last_name</th>
                <th>horário</th>
                <th>mensagem</th>
        </tr>
        `
    )
    $('.linha_dinamica').remove();
    for (let i = 0; i < data.length; i++) {
        var new_row = $(`
            <tr class='linha_dinamica'>
                <td class='linha_dinamica'>${i+1}</td>
                <td class='linha_dinamica'>${data[i]['message_id']}</td>
                <td class='linha_dinamica'>${data[i]['user_id']}</td>
                <td class='linha_dinamica'>${data[i]['first_name']}</td>
                <td class='linha_dinamica'>${data[i]['last_name']}</td>
                <td class='linha_dinamica'>${converterTimestamp(data[i]['timestamp'])}</td>
                <td class='linha_dinamica'>${data[i]['text_msg']}</td>
              </tr class='linha_dinamica'>`)
        $('#tabela').append(new_row);
    }
}

function converterTimestamp(timestamp) {
    const date = new Date(timestamp * 1000);

    // Obter os componentes da data
    const day = String(date.getDate()).padStart(2, '0');
    const monthNames = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"];
    const month = monthNames[date.getMonth()]; // Nome do mês em abreviação
    const year = date.getFullYear();
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');

    // Formatar a data
    const formattedTime = `${day}/${month}/${year} ${hours}:${minutes}`;

    return formattedTime;
}

// preencher dados ao iniciar a página
buscarTodasMensagens()