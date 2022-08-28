document.addEventListener('DOMContentLoaded', () => {
  const output = document.querySelector('#output');

  const getTable = (row, col) => {
    console.log(row, col);
    const ret = [];

    for (let i = 0; i < col; i++) {
      const newRow = [];
      for (let j = 0; j < row; j++) {
        if (i % 2 == 0) newRow.push(row * i + j);
        else newRow.unshift(row * i + j);
      }
      ret.push(newRow);
    }

    return ret[0].map((_, i) => ret.map((r) => r[i]));
  };

  const removeAllChildNodes = (parent) => {
    while (parent.firstChild) {
      parent.removeChild(parent.firstChild);
    }
  };

  document.getElementById('inputs').onsubmit = (e) => {
    const data = new FormData(e.target)
    const rows = data.get('rows');
    const cols = data.get('cols');

    removeAllChildNodes(output);
    const gridBox = document.createElement('div');
    gridBox.classList.add('grid');
    gridBox.style['display'] = 'grid';
    gridBox.style['grid-template-columns'] = `repeat(${cols}, 1fr)`;

    const table = getTable(rows, cols);
    table.map((row, i) => {
      row.map((num, j) => {
        const item = document.createElement('div');
        item.style['justify-self'] = 'center';
        item.style['align-self'] = 'center';
        item.classList.add('item');
        item.textContent = num;
        gridBox.appendChild(item);
      });
    });
    output.appendChild(gridBox);

    return false;
  };
});
