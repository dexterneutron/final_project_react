
    import React, {Component} from 'react';
    import Articles  from './components/articles';

    class App extends Component {

      state = {
        articles: []
      }

      componentDidMount() {
        fetch('http://127.0.0.1:5000/api/articles')
        .then(res => res.json())
        .then((data) => {
          this.setState({ articles: data })
          console.log(data)
        })
        .catch(console.log)
      }

      render () {
        return ( 
          <div>
          <nav class="navbar navbar-dark bg-dark">
          <a class="navbar-brand" href="#">
          Latest News
          </a>
          </nav>
          <div class="container mt-3 mb-3">
          <Articles articles={this.state.articles} />
          </div>
          </div>
        );
      }
    }

    export default App;