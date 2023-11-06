document.addEventListener('DOMContentLoaded', function () {
  const taskInput = document.getElementById('taskInput');
  const addTaskButton = document.getElementById('addTask');
  const taskList = document.getElementById('taskList');
  const deleteCompletedButton = document.getElementById('delete-completed');
  const taskPriority = document.getElementById('taskPriority');
  const taskSorting = document.getElementById('taskSorting');
// This is where I used an API
// An API is a way for multiple computer programs to communicate with each other
// This is done by sending and receiving data

// Loads the saved tasks from Chrome Storage when the extension loads
  chrome.storage.sync.get(['tasks'], function (result) {
    if (result.tasks) {
      result.tasks.forEach((task) => {
        const taskItem = document.createElement('li');
        taskItem.textContent = task.text;
        taskItem.dataset.priority = task.priority;
        if (task.completed) {
          taskItem.classList.add('completed');
        }
        taskList.appendChild(taskItem);
      });
    }
  });

// Adds click event listener to a button for input, adding, clearing, saving, and sorting tasks
  addTaskButton.addEventListener('click', function () {
    const taskText = taskInput.value.trim();
    if (taskText) {
      addTask(taskText);
      taskInput.value = '';
      saveTasksToStorage(); // Save tasks to Chrome Storage
      sortTasks(taskSorting.value);
    }
  });

// Waits for user to press Enter key in input field and adds task if input isn't empty
  taskInput.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
      const taskText = taskInput.value.trim();
      if (taskText) {
        addTask(taskText);
        taskInput.value = '';
        saveTasksToStorage();
        sortTasks(taskSorting.value);
      }
    }
  });

// Waits for user to click on a task list, then it saves to storage, and sorts
  taskList.addEventListener('click', function (e) {
    if (e.target.tagName === 'LI') {
      toggleTaskCompletion(e.target);
      saveTasksToStorage();
      sortTasks(taskSorting.value);
    }
  });

// Once user clicks, deletes completed tasks, saves, and sorts
  deleteCompletedButton.addEventListener('click', function () {
    removeCompletedTasks();
    saveTasksToStorage();
    sortTasks(taskSorting.value);
  });

// Waits for change event and sorts
  taskSorting.addEventListener('change', function () {
    sortTasks(taskSorting.value);
  });

// Adds task to list with text and priority, then sorts tasks
  function addTask(taskText) {
    const taskItem = document.createElement('li');
    const priority = taskPriority.value;
    taskItem.textContent = `${taskText} (Priority: ${priority})`;
    taskItem.dataset.priority = priority;
    taskList.appendChild(taskItem);
    sortTasks(taskSorting.value);
  }

// Looks at task's completion status and updates delete button's visibility
  function toggleTaskCompletion(taskItem) {
    taskItem.classList.toggle('completed');
    deleteCompletedButton.style.display = hasCompletedTasks() ? 'block' : 'none';
  }

// Checks if there's completed tasks in task list
  function hasCompletedTasks() {
    return taskList.querySelector('.completed') !== null;
  }

// Removes completed tasks from list and hides delete button
  function removeCompletedTasks() {
    const completedTasks = taskList.querySelectorAll('.completed');
    completedTasks.forEach(function (taskItem) {
      taskItem.remove();
    });
    deleteCompletedButton.style.display = 'none';
  }

// Sorts tasks based on priority or completion status
  function sortTasks(sortBy) {
    const tasks = Array.from(taskList.children);

    if (sortBy === 'priority') {
      tasks.sort((a, b) => {
        const priorityOrder = { high: 0, medium: 1, low: 2 };
        const priorityA = priorityOrder[a.dataset.priority];
        const priorityB = priorityOrder[b.dataset.priority];
        return priorityA - priorityB;
      });
    } else if (sortBy === 'completion') {
      tasks.sort((a, b) => {
        const completedA = a.classList.contains('completed');
        const completedB = b.classList.contains('completed');
        if (completedA === completedB) {
          return 0;
        } else if (completedA && !completedB) {
          return -1;
        } else {
          return 1;
        }
      });
    }
    while (taskList.firstChild) {
      taskList.removeChild(taskList.firstChild);
    }
    tasks.forEach((taskItem) => {
      taskList.appendChild(taskItem);
    });
  }

// Saves tasks from extension to Chrome storage as objects with text, priority, and completion status
  function saveTasksToStorage() {
    const tasks = Array.from(taskList.children).map((taskItem) => {
      return {
        text: taskItem.textContent,
        priority: taskItem.dataset.priority,
        completed: taskItem.classList.contains('completed'),
      };
    });
    chrome.storage.sync.set({ tasks: tasks });
  }
});