export default class TableCellEditing{
    constructor(table) {
        this.tbody = table.querySelecter('tbody')
    }
    init(){
        const tds = this.tbody.querySelecter('td')
        tds.forEach(td => {
            td.setAttribute('contenteditable', true);
            td.addEventListener('click', )
        });
    }
}