const XLSX = require('xlsx');
const fs = require('fs');
const path = require('path');

/**
 * 读取Excel文件的第一列数据
 * @param {string} filePath - Excel文件路径
 * @returns {Array} 第一列的数据数组
 */
function readExcelFirstColumn(filePath) {
    try {
        // 检查文件是否存在
        if (!fs.existsSync(filePath)) {
            console.error(`错误: 文件不存在 - ${filePath}`);
            return [];
        }

        // 读取Excel文件
        const workbook = XLSX.readFile(filePath);
        
        // 获取第一个工作表
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        
        // 将工作表转换为JSON
        const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
        
        // 获取第一列数据
        const firstColumn = jsonData.map(row => row[0]).filter(item => 
            item !== undefined && item !== null && item.toString().trim() !== ''
        );
        
        console.log(`成功读取Excel文件: ${filePath}`);
        console.log(`第一列数据数量: ${firstColumn.length}`);
        
        return firstColumn;
        
    } catch (error) {
        console.error(`读取Excel文件时出错: ${error.message}`);
        return [];
    }
}

/**
 * 读取Excel文件的第一列数据，可选择是否包含表头
 * @param {string} filePath - Excel文件路径
 * @param {boolean} hasHeader - 是否包含表头，默认true
 * @returns {Array} 第一列的数据数组
 */
function readExcelFirstColumnWithHeader(filePath, hasHeader = true) {
    try {
        // 检查文件是否存在
        if (!fs.existsSync(filePath)) {
            console.error(`错误: 文件不存在 - ${filePath}`);
            return [];
        }

        // 读取Excel文件
        const workbook = XLSX.readFile(filePath);
        
        // 获取第一个工作表
        const sheetName = workbook.SheetNames[0];
        const worksheet = workbook.Sheets[sheetName];
        
        // 将工作表转换为JSON
        const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
        
        // 获取第一列数据
        let firstColumn = jsonData.map(row => row[0]).filter(item => 
            item !== undefined && item !== null && item.toString().trim() !== ''
        );
        
        // 如果不包含表头，跳过第一行
        if (!hasHeader && firstColumn.length > 0) {
            firstColumn = firstColumn.slice(1);
        }
        
        console.log(`成功读取Excel文件: ${filePath}`);
        console.log(`第一列数据数量: ${firstColumn.length}`);
        
        return firstColumn;
        
    } catch (error) {
        console.error(`读取Excel文件时出错: ${error.message}`);
        return [];
    }
}

/**
 * 读取指定目录下的Excel文件
 * @param {string} directory - 目录路径
 * @param {string} filename - 文件名
 * @returns {Array} 第一列的数据数组
 */
function readExcelFromDirectory(directory, filename) {
    const filePath = path.join(directory, filename);
    return readExcelFirstColumn(filePath);
}

module.exports = {
    readExcelFirstColumn,
    readExcelFirstColumnWithHeader,
    readExcelFromDirectory
}; 