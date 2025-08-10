import React from 'react';
import { format } from 'date-fns';
import { Calendar, Tag, Clock } from 'lucide-react';

const TodoItem = ({ todo, onUpdate, onDelete, onEdit }) => {
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

  return (
    <div className="card todo-item hover:shadow-md transition-all duration-200">
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
              onClick={() => onEdit(todo.id)}
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
    </div>
  );
};

export default TodoItem;
