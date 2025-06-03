# Festus Matsitsa Bombo - Data Science Portfolio

A comprehensive data science portfolio website built with Streamlit, showcasing expertise in data analysis, machine learning, and visualization.

## Features

- **Professional Portfolio**: Complete overview of experience, skills, and education
- **Interactive Data Science Toolkit**: Real-time data analysis, visualization, and machine learning tools
- **Resume Download**: Direct PDF download functionality
- **Responsive Design**: Mobile-friendly interface with professional styling
- **Multi-page Navigation**: Organized sections for easy exploration

## Deployment Options

### Vercel Deployment

1. Connect your GitHub repository to Vercel
2. Vercel will automatically detect the configuration from `vercel.json`
3. The app will be deployed with proper Python runtime support

### Streamlit Cloud Deployment

1. Push your code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy directly to Streamlit Cloud

### Heroku Deployment

1. Install Heroku CLI
2. Create a new Heroku app
3. Deploy using the included `Procfile` and `setup.sh`

### Local Development

```bash
# Install dependencies
pip install streamlit pandas numpy matplotlib seaborn plotly scikit-learn scipy

# Run the application
streamlit run app.py
```

## Project Structure

```
├── app.py                          # Main application file
├── pages/
│   ├── 1_Experience.py            # Professional experience page
│   ├── 2_Skills.py                # Skills and expertise page
│   └── 3_Data_Science_Toolkit.py  # Interactive data science tools
├── utils/
│   ├── data_analysis.py           # Data analysis utilities
│   └── ml_models.py               # Machine learning utilities
├── assets/
├── attached_assets/
│   └── My Resume.pdf              # Resume file
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── vercel.json                    # Vercel deployment config
├── Procfile                       # Heroku deployment config
├── setup.sh                      # Heroku setup script
└── netlify.toml                   # Netlify deployment config
```

## Data Science Toolkit Features

- **Data Upload & Analysis**: Support for CSV file upload and analysis
- **Exploratory Data Analysis**: Automated EDA with statistics and visualizations
- **Feature Engineering**: Data preprocessing and feature creation tools
- **Machine Learning**: Classification, regression, and clustering models
- **Interactive Visualizations**: Dynamic charts and plots
- **Statistical Analysis**: Comprehensive statistical testing and analysis

## Technologies Used

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Statistical Analysis**: SciPy

## Contact Information

- **Name**: Festus Matsitsa Bombo
- **Position**: Data Scientist
- **Education**: BSc Computer Science, Pwani University (2022-2027)
- **Experience**: Freelance Data Scientist on Fiverr & Upwork (2021-Present)

## License

This project is open source and available under the MIT License.