import React from 'react'

    const Articles = ({ articles }) => {
      return (
     <div class="list-group">
        {articles.map((article) => (
            <div>
            <a href={article.id} class="list-group-item list-group-item-action flex-column align-items-start">
            <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1"> {article.title}</h5>
            </div>
            <p class="mb-1">Source: {article.source}</p>
            </a>
            </div>
        ))}
    </div>
     
     
     
     
     
     
     
     
     
     
     
     
     
     )









    };

    export default Articles