const navs = document.querySelectorAll('.nav-list li');
const cube = document.querySelector('.box');
const sections = document.querySelectorAll('.section');

const resumeLists = document.querySelectorAll('.resume-list');
const resumeBoxs = document.querySelectorAll('.resume-box');

const portfolioLists = document.querySelectorAll('.portfolio-list');
const portfolioBoxs = document.querySelectorAll('.portfolio-box');

// Xử lý khi nhấn vào mục trong thanh điều hướng
navs.forEach((nav, idx) => {
    nav.addEventListener('click', () => {
        // Loại bỏ lớp 'active' khỏi mục đang hoạt động
        document.querySelector('.nav-list li.active')?.classList.remove('active');
        // Thêm lớp 'active' vào mục được nhấn
        nav.classList.add('active');

        // Xoay khối lập phương dựa trên chỉ số
        cube.style.transform = `rotateY(${idx * -90}deg)`;

        document.querySelector('.section.active')?.classList.remove('active');
        sections[idx].classList.add('active');

        const arrSecs = Array.from(sections).slice(1, -1);
        arrSecs.forEach(section => {
            if (section.classList.contains('active')) {
                sections[4].classList.add('action-contact');
            }
        });
        if (sections[0].classList.contains('active')) {
            sections[4].classList.remove('action-contact');
        }
    });
});

// Phần Resume khi nhấn vào tab-list
resumeLists.forEach((list, idx) => {
    list.addEventListener('click', () => {
        // Loại bỏ lớp 'active' khỏi mục và hộp đang hoạt động
        document.querySelector('.resume-list.active')?.classList.remove('active');
        document.querySelector('.resume-box.active')?.classList.remove('active');

        // Thêm lớp 'active' vào mục và hộp được nhấn
        list.classList.add('active');
        resumeBoxs[idx].classList.add('active');
    });
});

// Phần Portfolio khi nhấn vào tab-list
portfolioLists.forEach((list, idx) => {
    list.addEventListener('click', () => {
        // Loại bỏ lớp 'active' khỏi mục và hộp đang hoạt động
        document.querySelector('.portfolio-list.active')?.classList.remove('active');
        document.querySelector('.portfolio-box.active')?.classList.remove('active');

        // Thêm lớp 'active' vào mục và hộp được nhấn
        list.classList.add('active');
        portfolioBoxs[idx].classList.add('active');
    });
});

setTimeout(() => {
    sections[4].classList.remove('active');
}, 1500);
