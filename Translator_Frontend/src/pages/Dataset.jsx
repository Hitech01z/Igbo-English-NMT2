import DatasetTable from "../components/dataset/DatasetTable";
import SearchBar from "../components/dataset/SearchBar";
import FilterBar from "../components/dataset/FilterBar";

export default function Dataset() {
  return (
    <div className="space-y-6">

      <div>
        <h1 className="text-3xl font-bold">
          Dataset Explorer
        </h1>

        <p className="text-gray-500 mt-2">
          Browse all English-Igbo sentence pairs.
        </p>
      </div>

      <div className="grid md:grid-cols-2 gap-4">

        <SearchBar />

        <FilterBar />

      </div>

      <DatasetTable />

    </div>
  );
}