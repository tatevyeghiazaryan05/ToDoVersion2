import React, { useState } from 'react';
import TodoItem from './TodoItem';
import { format } from 'date-fns';
import { Calendar, Tag, Clock } from 'lucide-react';

const TodoList = ({ todos, onUpdate, onDelete }) => {
  const [editingId, setEditingId] = useState(null);

  if (todos.length === 0) {
    return (
      <div className="card text-center py-12">
        <div className="w-16 h-16 mx-auto mb-4 bg-secondary-100 rounded-full flex items-center justify-center">
          <svg className="w-8 h-8 text-secondary-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
        </div>
        <h3 className="text-lg font-medium text-secondary-900 mb-2">No todos yet</h3>
        <p className="text-secondary-600">Get started by creating your first todo item!</p>
      </div>
    );
  }

  const handleEdit = (todoId) => {
    setEditingId(todoId);
  };

  const handleSave = async (todoId, updates) => {
    await onUpdate(todoId, updates);
    setEditingId(null);
  };

  const handleCancel = () => {
    setEditingId(null);
  };

  const getStatusColor = (status) => {
    switch (status) {
      case 'completed':
        return 'bg-green-100 text-green-800 border-green-200';
      case 'in_progress':
        return 'bg-yellow-100 text-yellow-800 border-yellow-200';
      case 'pending':
        return 'bg-red-100 text-red-800 border-red-200';
      default:
        return 'bg-secondary-100 text-secondary-800 border-secondary-200';
    }
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'completed':
        return 'Completed';
      case 'in_progress':
        return 'In Progress';
      case 'pending':
        return 'Pending';
      default:
        return status;
    }
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case 'high':
        return 'bg-red-500';
      case 'medium':
        return 'bg-yellow-500';
      case 'low':
        return 'bg-green-500';
      default:
        return 'bg-secondary-400';
    }
  };

  return (
    <div className="space-y-4">
      {todos.map((todo) => (
        <div
          key={todo.id}
          className="card todo-item hover:shadow-md transition-all duration-200"
        >
          <div className="flex items-start space-x-4">
            {/* Status Checkbox */}
            <div className="flex-shrink-0 pt-1">
              <input
                type="checkbox"
                checked={todo.status === 'completed'}
                onChange={() => {
                  const newStatus = todo.status === 'completed' ? 'pending' : 'completed';
                  onUpdate(todo.id, { status: newStatus });
                }}
                className="checkbox-custom"
              />
            </div>

            {/* Todo Content */}
            <div className="flex-1 min-w-0">
              <div className="flex items-start justify-between">
                <div className="flex-1">
                  <h3 className={`text-lg font-medium ${
                    todo.status === 'completed' ? 'line-through text-secondary-500' : 'text-secondary-900'
                  }`}>
                    {todo.title}
                  </h3>
                  <p className={`mt-1 text-sm ${
                    todo.status === 'completed' ? 'text-secondary-400' : 'text-secondary-600'
                  }`}>
                    {todo.description}
                  </p>
                </div>

                {/* Status Badge */}
                <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border ${getStatusColor(todo.status)}`}>
                  {getStatusText(todo.status)}
                </span>
              </div>

              {/* Meta Information */}
              <div className="mt-3 flex flex-wrap items-center gap-4 text-sm text-secondary-500">
                {/* Category */}
                <div className="flex items-center space-x-1">
                  <Tag className="h-4 w-4" />
                  <span>{todo.category}</span>
                </div>

                {/* Due Date */}
                {todo.due_date && (
                  <div className="flex items-center space-x-1">
                    <Calendar className="h-4 w-4" />
                    <span>{format(new Date(todo.due_date), 'MMM dd, yyyy')}</span>
                  </div>
                )}

                {/* Created Date */}
                <div className="flex items-center space-x-1">
                  <Clock className="h-4 w-4" />
                  <span>Created {format(new Date(todo.created_at || Date.now()), 'MMM dd, yyyy')}</span>
                </div>
              </div>

              {/* Actions */}
              <div className="mt-4 flex items-center space-x-3">
                <button
                  onClick={() => handleEdit(todo.id)}
                  className="text-sm text-primary-600 hover:text-primary-700 font-medium transition-colors"
                >
                  Edit
                </button>
                <button
                  onClick={() => onDelete(todo.id)}
                  className="text-sm text-red-600 hover:text-red-700 font-medium transition-colors"
                >
                  Delete
                </button>
              </div>
            </div>
          </div>

          {/* Edit Form */}
          {editingId === todo.id && (
            <TodoEditForm
              todo={todo}
              onSave={handleSave}
              onCancel={handleCancel}
            />
          )}
        </div>
      ))}
    </div>
  );
};

// Todo Edit Form Component
const TodoEditForm = ({ todo, onSave, onCancel }) => {
  const [formData, setFormData] = useState({
    title: todo.title,
    description: todo.description,
    category: todo.category,
    status: todo.status,
    due_date: todo.due_date ? format(new Date(todo.due_date), 'yyyy-MM-dd') : '',
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(todo.id, formData);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  return (
    <form onSubmit={handleSubmit} className="mt-4 pt-4 border-t border-secondary-200">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-1">
            Title
          </label>
          <input
            type="text"
            name="title"
            value={formData.title}
            onChange={handleChange}
            className="input-field"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-1">
            Category
          </label>
          <input
            type="text"
            name="category"
            value={formData.category}
            onChange={handleChange}
            className="input-field"
            required
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-1">
            Status
          </label>
          <select
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="input-field"
          >
            <option value="pending">Pending</option>
            <option value="in_progress">In Progress</option>
            <option value="completed">Completed</option>
          </select>
        </div>

        <div>
          <label className="block text-sm font-medium text-secondary-700 mb-1">
            Due Date
          </label>
          <input
            type="date"
            name="due_date"
            value={formData.due_date}
            onChange={handleChange}
            className="input-field"
          />
        </div>

        <div className="md:col-span-2">
          <label className="block text-sm font-medium text-secondary-700 mb-1">
            Description
          </label>
          <textarea
            name="description"
            value={formData.description}
            onChange={handleChange}
            rows={3}
            className="input-field"
            required
          />
        </div>
      </div>

      <div className="mt-4 flex justify-end space-x-3">
        <button
          type="button"
          onClick={onCancel}
          className="btn-secondary"
        >
          Cancel
        </button>
        <button
          type="submit"
          className="btn-primary"
        >
          Save Changes
        </button>
      </div>
    </form>
  );
};

export default TodoList;
