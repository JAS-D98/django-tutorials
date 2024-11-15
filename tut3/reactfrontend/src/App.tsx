import './App.css'
import { BrowserRouter, Routes, Route} from 'react-router-dom'
import Details from './components/Details'
import EditDetails from './components/EditDetails'

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Details/>}/>
          <Route path='/edit' element={<EditDetails/>}/>
        </Routes>
      </BrowserRouter>
    </div>
  )
}

export default App