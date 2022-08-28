document.addEventListner('DOMContentLoaded', () => {
   const table = (row, col) => {
    const ret = [];

    for (const i in Array(row).keys()) {
      const newRow = [];
      for (const j in Array(col).keys()) {
        if (row % 2 === 0) newRow.push(row * i + j + 1);
        else newRow.unshift(row * i + j + 1);
      }
      ret.push(newRow);
    }

    return ret[0].map((_, i) => arr.map((r) => r[i]));
  };

  window.table = table;
});
