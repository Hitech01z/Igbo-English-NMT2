import { useEffect, useState }
from "react";

import {
  getDataset,
}
from "../services/datasetService";

export function useDataset() {

  const [rows, setRows] =
    useState([]);

  useEffect(() => {

    getDataset()
      .then(setRows);

  }, []);

  return rows;
}