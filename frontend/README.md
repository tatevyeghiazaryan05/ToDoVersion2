# Todo App Frontend

A modern, responsive React frontend for the Todo application with a beautiful UI built using Tailwind CSS.

## Features

- 🚀 **Modern React 18** with hooks and functional components
- 🎨 **Beautiful UI** built with Tailwind CSS
- 🔐 **User Authentication** with login/signup and email verification
- ✅ **Todo Management** - Create, read, update, delete todos
- 🔍 **Search & Filtering** - Search todos and filter by status/category
- 📱 **Responsive Design** - Works on all devices
- 🎯 **Real-time Updates** - Instant feedback and state management
- 🔔 **Toast Notifications** - User-friendly feedback messages
- 📅 **Date Handling** - Due dates and creation dates
- 🎨 **Custom Components** - Reusable UI components

## Tech Stack

- **React 18** - Modern React with hooks
- **React Router 6** - Client-side routing
- **Tailwind CSS** - Utility-first CSS framework
- **React Hook Form** - Form handling and validation
- **Axios** - HTTP client for API calls
- **Lucide React** - Beautiful icons
- **Date-fns** - Date manipulation utilities
- **React Hot Toast** - Toast notifications

## Prerequisites

- Node.js 16+ 
- npm or yarn
- Backend API running (FastAPI)

## Installation

1. **Navigate to the frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## Project Structure

```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── auth/
│   │   │   ├── Login.js
│   │   │   └── SignUp.js
│   │   └── dashboard/
│   │       ├── Dashboard.js
│   │       ├── Header.js
│   │       ├── TodoList.js
│   │       ├── TodoItem.js
│   │       └── AddTodoModal.js
│   ├── contexts/
│   │   └── AuthContext.js
│   ├── services/
│   │   ├── authService.js
│   │   └── todoService.js
│   ├── App.js
│   ├── index.js
│   ├── index.css
│   └── App.css
├── package.json
├── tailwind.config.js
└── postcss.config.js
```

## Configuration

### Backend API

The frontend is configured to connect to your FastAPI backend. Make sure:

1. **Backend is running** on `http://localhost:8000`
2. **CORS is enabled** in your FastAPI app
3. **API endpoints** match the expected structure

### Environment Variables

Create a `.env` file in the frontend directory if needed:

```env
REACT_APP_API_URL=http://localhost:8000
```

## Usage

### Authentication

1. **Sign Up**: Create a new account with email verification
2. **Login**: Sign in with your credentials
3. **Logout**: Use the user menu in the header

### Todo Management

1. **Create Todo**: Click "Add Todo" button
2. **Edit Todo**: Click "Edit" on any todo item
3. **Delete Todo**: Click "Delete" on any todo item
4. **Mark Complete**: Use the checkbox to toggle status
5. **Search**: Use the search bar to find specific todos
6. **Filter**: Use status and category filters

### Features

- **Real-time Updates**: Changes are reflected immediately
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Form Validation**: Client-side validation with helpful error messages
- **Loading States**: Visual feedback during API calls
- **Error Handling**: User-friendly error messages

## API Integration

The frontend integrates with your FastAPI backend through these services:

### Auth Service (`/api/user/auth/`)
- `POST /sign-up` - User registration
- `POST /verify` - Email verification
- `POST /login` - User authentication

### Todo Service (`/api/todo/`)
- `GET /get/all/todo` - Fetch all todos
- `POST /add/todo` - Create new todo
- `PUT /change/{id}` - Update todo
- `DELETE /delete/todo/{id}` - Delete todo
- `GET /get/todo/{id}` - Get specific todo

## Customization

### Styling

- **Tailwind CSS**: Modify `tailwind.config.js` for custom colors and themes
- **Custom CSS**: Add custom styles in `src/App.css`
- **Component Styling**: Each component uses Tailwind utility classes

### Components

- **Reusable Components**: All components are modular and reusable
- **Props Interface**: Components accept props for customization
- **Event Handlers**: Customizable event handlers for user interactions

## Building for Production

1. **Build the project:**
   ```bash
   npm run build
   ```

2. **Serve the build:**
   ```bash
   npm install -g serve
   serve -s build
   ```

## Troubleshooting

### Common Issues

1. **Backend Connection Error**
   - Ensure backend is running on port 8000
   - Check CORS configuration
   - Verify API endpoints

2. **Build Errors**
   - Clear `node_modules` and reinstall
   - Check Node.js version compatibility
   - Verify all dependencies are installed

3. **Styling Issues**
   - Ensure Tailwind CSS is properly configured
   - Check PostCSS configuration
   - Verify CSS imports in components

### Development Tips

- Use React Developer Tools for debugging
- Check browser console for errors
- Use Network tab to monitor API calls
- Test responsive design on different screen sizes

## Contributing

1. Follow the existing code structure
2. Use consistent naming conventions
3. Add proper error handling
4. Test on different devices
5. Update documentation as needed

## License

This project is part of the Todo application frontend.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Check browser console for errors
4. Verify backend connectivity
