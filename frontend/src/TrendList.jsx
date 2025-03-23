import { useEffect, useState } from "react";
import axios from "axios";

const TrendList = ({ category }) => {
  const [trends, setTrends] = useState([]);

  useEffect(() => {
    axios.get(`http://localhost:8000/trends/${category}`)
      .then(response => setTrends(response.data.trends))
      .catch(error => console.error(error));
  }, [category]);

  return (
    <div>
      <h2>{category} Trends</h2>
      <ul>
        {trends.map((trend, index) => (
          <li key={index}>{trend.title}</li>
        ))}
      </ul>
    </div>
  );
};

export default TrendList;
