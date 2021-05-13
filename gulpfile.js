const fs = require('fs');
const gulp = require('gulp');
const autoprefixer = require('gulp-autoprefixer');
const cleanCSS = require('gulp-clean-css');
const include = require('gulp-include');
const eslint = require('gulp-eslint');
const isFixed = require('gulp-eslint-if-fixed');
const babel = require('gulp-babel');
const rename = require('gulp-rename');
const sass = require('gulp-sass');
const sassLint = require('gulp-sass-lint');
const uglify = require('gulp-uglify');

const config = {
  src: {
    scssPath: './src/scss',
    jsPath: './src/js'
  },
  dist: {
    cssPath: './static/css',
    jsPath: './static/js',
    fontPath: './static/fonts'
  },
  packagesPath: './node_modules'
};

function lintSCSS(src) {
  return gulp.src(src)
    .pipe(sassLint())
    .pipe(sassLint.format())
    .pipe(sassLint.failOnError());
}

function buildCSS(src, dest) {
  dest = dest || config.dist.cssPath;

  return gulp.src(src)
    .pipe(sass({
      includePaths: [config.src.scssPath, config.packagesPath]
    })
      .on('error', sass.logError))
    .pipe(cleanCSS())
    .pipe(autoprefixer({
      cascade: false
    }))
    .pipe(rename({
      extname: '.min.css'
    }))
    .pipe(gulp.dest(dest));
}

function lintJS(src, dest) {
  dest = dest || config.src.jsPath;

  return gulp.src(src)
    .pipe(eslint({
      fix: true
    }))
    .pipe(eslint.format())
    .pipe(isFixed(dest));
}

function buildJS(src, dest) {
  dest = dest || config.dist.jsPath;

  return gulp.src(src)
    .pipe(include({
      includePaths: [config.packagesPath, config.src.jsPath]
    }))
    .on('error', console.log) // eslint-disable-line no-console
    .pipe(babel())
    .pipe(uglify())
    .pipe(rename({
      extname: '.min.js'
    }))
    .pipe(gulp.dest(dest));
}

//
// CSS
//
gulp.task('scss-lint', () => {
  return lintSCSS(`${config.src.scssPath}/*.scss`);
});

gulp.task('scss-build', () => {
  return buildCSS(`${config.src.scssPath}/style.scss`);
});

gulp.task('css', gulp.series('scss-lint', 'scss-build'));

//
// JavaScript
//

gulp.task('js-lint', () => {
  return lintJS([`${config.src.jsPath}/*.js`], config.src.jsPath);
});

gulp.task('js-build', () => {
  return buildJS(`${config.src.jsPath}/script.js`, config.dist.jsPath);
});

gulp.task('js', gulp.series('js-lint', 'js-build'));


gulp.task('watch', () => {
  gulp.watch(`${config.src.scssPath}/**/*.scss`, 'css');
  gulp.watch(`${config.src.jsPath}/**/*.js`, 'js');
});

gulp.task('default', gulp.series('css', 'js'));
